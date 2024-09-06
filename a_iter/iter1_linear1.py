"""
CSE 3110: Iterative Algorithms
Linear Search
"""

# Complete this function only...

def search(data, val):
    "Linear search algorithm"
    yield "Not implemented!"


# DO NOT EDIT any of the code below.

from resource.randomData import randomData

def main():
    data = randomData()
    val = int(input("Value to search for: "))
    msg = "The value {} was found at the following indices:"
    print(msg.format(val))
    for index in search(data, val):
        print(index)

main()
