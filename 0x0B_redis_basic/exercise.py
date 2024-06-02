#!/usr/bin/env python3
"""
An excercise in learning Redis and using it as a Caching system
"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that records and returns how many
    times the decorated method is called
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> method:
        """A wrapper for our decorator"""

        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores and returns input
    and output for the decorated method
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for our decorator"""

        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache():
    """A Caching Class using Redis"""

    def __init__(self) -> None:
        """Initializes Cache class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores Data and returns it as a string"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Returns value stored at Key"""

        data = self._redis.get(key)

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """Parametrizes Cache.get to str"""

        data = self._redis.get(key)

        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametrize Cache.get to int"""

        data = self._redis.get(key)

        return int(data)


def replay(self, method: Callable) -> None:
        """Displays the call history of a function."""

        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        call_count = int(self._redis.get(method.__qualname__) or 0)

        print(f"{method.__qualname__} was called {call_count} times:")

        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        for i, o in zip(inputs, outputs):
            i = i.decode('utf-8') if isinstance(i, bytes) else i
            o = o.decode('utf-8') if isinstance(o, bytes) else o
            print(f"{method.__qualname__}(*{eval(i)}) -> {o}")
