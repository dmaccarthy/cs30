"""
CSE 3310: Recursive Programming
Recursion — Example 3
"""

def factorial(n):
    "Calculate factorial iteratively"
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

print(factorial(7))
