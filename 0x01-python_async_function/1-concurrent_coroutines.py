#!/usr/bin/env python3
"""Implements execution of multiple coroutines."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Waits for a random delay between 0 and `max_delay` seconds `n` times,
    asynchronously, and returns a list of the resulting delay times.

    Parameters:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        list: A list of delay times, each delay representing the time waited
        for each iteration.
    """
    results = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(results)
