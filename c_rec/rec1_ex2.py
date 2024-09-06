"""
CSE 3310: Recursive Programming
Recursion — Example 2
"""

def factorial(n):
    "Calculate factorial recursively"
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(7))
