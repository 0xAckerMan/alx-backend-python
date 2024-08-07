#!/usr/bin/python3
""" async/await"""
import random
import asyncio


async def wait_random(max_delay: int = 10) = -> float:
    """
    delays for a random amount of seconds
    Args::
        max_delay(int): the set max delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
