#!/usr/bin/env python3
""" Basic asynch generator."""

import asyncio
import random


async def async_generator():
    """Basic async syntax of asyc generator."""
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
