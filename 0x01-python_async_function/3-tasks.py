#!/usr/bin/env python3
"""Creates an asyncio task."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task for the wait_random function with the specified
    maximum delay.

    Parameters:
        max_delay (int): The maximum delay time in seconds for the wait_random
            function.

    Returns:
        asyncio.Task: An asyncio task that executes the wait_random function
        with the specified maximum delay.
    """
    return asyncio.create_task(wait_random(max_delay))
