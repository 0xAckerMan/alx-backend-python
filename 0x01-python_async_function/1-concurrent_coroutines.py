#!/usr/bin/env python3
"""
import wait random from previous flile
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    runs a function multiple times(n) with delays(max_delay)

    Args::
        n(int): number of times to call the async function
        max_delay(int): amount of delay between function calls
    """
    delays = []
    active_tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(active_tasks):
        delay = await task
        delays.append(delay)
    return delays
