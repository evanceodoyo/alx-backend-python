#!/usr/bin/env python3

import asyncio
import random

"""Implements the basic async syntax."""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function to generate a random delay between 0 and 'max_delay',
    waits for that duration, and then returns the generated delay.

    Parameters:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The randomly generated delay.
    """
    s = random.uniform(0, max_delay)
    await asyncio.sleep(s)
    return s

if __name__ == "__main__":
    asyncio.run(wait_random())
