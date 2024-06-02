#!/usr/bin/env python3
"""
An excercise in learning Redis and using it as a Caching system
"""

import redis
import uuid
from typing import Union, Optional, Callable


class Cache():
    """A Caching Class using Redis"""

    def __init__(self) -> None:
        """Initializes Cache class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

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
