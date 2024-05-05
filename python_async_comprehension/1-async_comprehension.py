#!/usr/bin/env python3

"""
Import async_generator from the previous
task and then write a coroutine called
async_comprehension that takes no arguments.
"""

import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:

    """Collects then returns 10 random Numbers"""

    return [i async for i in async_generator()][:10]
