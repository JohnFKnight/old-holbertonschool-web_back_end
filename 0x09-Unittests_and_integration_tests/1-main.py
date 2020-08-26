#!/usr/bin/env python3

import requests
from functools import wraps
from typing import (Mapping,
                    Sequence,
                    Any,
                    Dict,
                    Callable,)

from utils import access_nested_map

nested_map = {}
path = ("a",)
print(access_nested_map(nested_map, path))

nested_map = {"a": 1}
path = ("a", "b")
print(access_nested_map(nested_map, path))
