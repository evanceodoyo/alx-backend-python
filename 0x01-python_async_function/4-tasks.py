#!/usr/bin/env python3
"""Executes executive concurrent tasks with random delays."""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute task_wait_random concurrently n times.

    Parameters:
        n (int): The number of times to execute task_wait_random.
        max_delay (int): The maximum delay time in seconds for each execution.

    Returns:
        List[float]: A sorted list of the times taken for each execution.
    """
    rs = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    return sorted(rs)
