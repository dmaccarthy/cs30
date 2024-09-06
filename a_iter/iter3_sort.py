"""
CSE 3110: Iterative Algorithms
Sorting Algorithms
"""

# Complete these functions only

def bubbleSort(data):
    "Bubble sort algorithm"
    return data


def insertionSort(data):
    "Insertion sort algorithm"
    return data


def selectionSort(data):
    "Selection sort algorithm"
    return data


# Specify the sorting algorithm to use
sortingAlgorithm = bubbleSort

# Specify how the data is to be ordered
def ascend(a, b):
    return b < a

def descend(a, b):
    return a < b

compare = ascend


# DO NOT EDIT any of the code below

from resource.randomData import randomData
from time import time


def main():
    data = randomData()
    t = time()
    data = sortingAlgorithm(data)
    t = time() - t
    for x in data:
        print(x)
    print("Sorting time: {:.3g} seconds".format(t))

main()

# Comparison of efficiencies...
#
