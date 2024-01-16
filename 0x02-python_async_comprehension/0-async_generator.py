#!/usr/bin/env python3
"""
Defining an Asynchronous function
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times for each time asynchronously
    with one second delay
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
