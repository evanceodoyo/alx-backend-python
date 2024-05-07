#!/usr/bin/env python3
"""Async generation and comprehension of random numbers."""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [i async for i in async_generator()]
