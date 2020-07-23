#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async."""
    list1: List[float] = []
    dly_list: List[float] = []
    for i in range(n):
        # dly_list.append(asyncio.ensure_future(wait_random(max_delay)))
        list1.append(asyncio.create_task(wait_random(max_delay)))
    for j in list1:
        dly_list.append(await j)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(wait_n(max_delay, n))
    return (dly_list)
