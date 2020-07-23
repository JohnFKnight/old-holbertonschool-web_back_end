#!/usr/bin/env python3
"""Parallel asynch comprehension."""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Parallel async comprehension."""
    s: float = time.perf_counter()
    await asyncio.gather[async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()]
    return (time.perf_counter() - s)
