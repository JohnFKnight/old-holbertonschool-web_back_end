#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """execute multiple coroutines at the same time with async."""

    elaspsed: float

    s = time.perf_counter()
    await wait_n(n, max_delay)
    # asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return (elapsed)
