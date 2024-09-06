"""
CSE 3310: Recursive Programming
Recursion
"""

DATA_SIZE = 50
MAX_NUM = 20


# Complete these functions only...

def bsearch(data, target, compare):
    "Find ONE occurrence of target in the data"
    pass

def findAll(data, target, compare):
    "Find ALL occurrences of target in the data"
    return bsearch(data, target, compare)


# DO NOT EDIT any of the code below.

import resource.randomData as r

def test():
    data = sorted(r.randomData(DATA_SIZE, MAX_NUM))
    target = int(input("Enter a number to search for: "))
    print("Data:", data)
    found = findAll(data, target, r.ascend)
    print("Data {} found at {}.".format(target, found))

test()
