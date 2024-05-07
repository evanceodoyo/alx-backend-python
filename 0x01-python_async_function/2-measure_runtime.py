#!/usr/bin/env python3
"""Measures for the average time taken to execute multiple coroutines"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken by the wait_n function to execute
    asynchronously.

    Parameters:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay time in seconds for each call to
            the wait_n function.

    Returns:
        float: The average time taken by the wait_n function to execute
        asynchronously.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
