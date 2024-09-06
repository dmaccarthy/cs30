"""
CSE 3310: Recursive Programming
Recursion — Example 1
"""

from random import randint

def randColor():
    return [randint(0, 255) for i in range(3)]

print(randColor())
