#!/usr/bin/env python3
"""Async generator producing random floats."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random floats within a range.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding
        random floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
