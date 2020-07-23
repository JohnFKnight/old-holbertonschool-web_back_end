#!/usr/bin/env python3
""" asynch comprehension."""

import asyncio
import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Basic async comprehension."""
    result = [i async for i in async_generator() if i < 10]
    return (result)