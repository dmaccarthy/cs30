"""
CSE 3310: Recursive Programming
Quick Sort
"""

DATA_SIZE = 50
MAX_NUM = 20
ASCENDING = True


# Complete these functions only...

def partition(data, ascend, left, right):
    pass

def quickSort(data, ascend, left=0, right=None):
    pass


# DO NOT EDIT any of the code below.

from resource.randomData import randomData

def main():
    original = randomData(DATA_SIZE, MAX_NUM)
    data = quickSort(original, ASCENDING)
    for item in data:
        print(item)

main()
