#!/usr/bin/env python3
""" asynch comprehension."""

import asyncio
from typing import List, Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]
    """Basic async comprehension."""
    result = [i async for i in async_generator()]
    return (result)
