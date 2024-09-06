"""
CSE 3110: Iterative Algorithms
Binary Search
"""

# Complete this function only...

def bsearch(data, number):
    "Binary search algorithm"
    left = 0
    right = len(data) - 1
    yield "Not implemented!"


# DO NOT EDIT any of the code below.

from resource.school import students

def main():
    data = students()
    num = int(input("Student number: "))
    for match in bsearch(data, num):
        print(match)

main()
