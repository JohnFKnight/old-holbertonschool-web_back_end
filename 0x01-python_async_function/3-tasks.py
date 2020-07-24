#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async."""

import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """execute multiple coroutines at the same time with async."""

    return asyncio.ensure_future(wait_random())
