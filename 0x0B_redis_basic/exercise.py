#!/usr/bin/env python3
"""
An excercise in learning Redis and using it as a Caching system
"""

import redis
import uuid
from typing import Union


class Cache():
    """A Caching Class using Redis"""

    def __init__(self) -> None:
        """Initializes Cache class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores Data and returns it as a string"""

        key = str(uuid.uuid4())

        if isinstance(data, (int, float)):
            data = str(data)

        self._redis.set(key, data)
        return key
