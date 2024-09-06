"""
CSE 3310: Recursive Programming
Merge Sort
"""

DATA_SIZE = 50
MAX_NUM = 20
ASCENDING = True


# Complete these functions only...

def merge(list1, list2, ascend):
    pass

def mergeSort(data, ascend):
    pass


# DO NOT EDIT any of the code below.

from resource.randomData import randomData

def main():
    original = randomData(DATA_SIZE, MAX_NUM)
    data = mergeSort(original, ASCENDING)
    for item in data:
        print(item)

main()
