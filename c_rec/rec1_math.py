"""
CSE 3310: Recursive Programming
Recursion
"""


# Complete these functions only...

def power(x, n):
    pass

def sumWhole(n):
    pass

def factor(n):
    yield None


# DO NOT EDIT any of the code below.

def test():
    # Input...
    n = int(input("Enter a whole number: "))
    x = float(input("Enter a number: "))

    # Processing...
    p = power(x, n)
    s = sumWhole(n)
    factors = factor(n)

    # Output...
    print("{}**{} = {}.".format(x, n, p))
    print("The sum of the first {} whole numbers is {}.".format(n, s))
    print("The prime factors of {} are:".format(n))
    for f in factors: print(f)

test()