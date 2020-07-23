#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """execute multiple coroutines at the same time with async."""

    elaspsed: float

    s = time.perf_counter()
    # await wait_n(max_delay, n)
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - s
    return (elapsed)
