"""
CSE 3110: Iterative Algorithms
Merging
"""

# Copy your favSort function from iter4_sort.py...

def favSort(data, **kwargs):
    return data


# Complete these functions.

def mergeSort(data, key, ascend=True):
    "Sort a list of dictionaries by splitting it into two lists, sorting them, and then merging."
    return []

def merge(data1, data2, key):
    "Merge two sorted lists into a new sorted list"
    return []


# DO NOT EDIT any of the code below.

from resource.school import students

def main():
    original = students()
    for key in original[0].keys():
        print(key)
    key = input("\nSort key? ")
    data = mergeSort(original, key)
    for s in data:
        print(s)

main()
