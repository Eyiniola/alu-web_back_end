#!/usr/bin/env python3
"""
Collects random numbers using async comprehension over async_generator.
"""


from typing import List
import importlib

async_generator = importlib.import_module("0-async_generator").async_generator

async def async_comprehension() -> List[int]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.
    
    Returns:
        List[int]: A list of 10 random integers collected from async_generator.
    """
    return [num async for num in async_generator()]


