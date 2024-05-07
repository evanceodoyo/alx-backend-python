#!/usr/bin/env python3
"""Async generator producing random floats."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates random floats within a range.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding
        random floats.
    """
    num: int = 0
    while num < 10:
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
        num += 1
