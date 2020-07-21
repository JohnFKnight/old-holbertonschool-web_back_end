#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

newlist = ["cat", "dog", "chipmunk"]

print(element_length.__annotations__)
print(element_length(newlist))
