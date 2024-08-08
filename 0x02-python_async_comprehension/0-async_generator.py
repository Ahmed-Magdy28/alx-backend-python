#!/usr/bin/env python3
"""
Async Comprehension for task 0
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Comprehension"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
