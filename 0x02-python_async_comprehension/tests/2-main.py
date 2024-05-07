#!/usr/bin/env python3

import sys
import asyncio

sys.path.append('../')
measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
