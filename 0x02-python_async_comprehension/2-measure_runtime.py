#!/usr/bin/env python3
"""Module for measuring runtime of asynchronous comprehensions."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of asynchronous comprehensions.

    This function measures the runtime of executing the async_comprehension
    coroutine four times using asyncio.gather().

    Returns:
        float: The total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
