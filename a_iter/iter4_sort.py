"""
CSE 3110: Iterative Algorithms
Sorting Algorithms
"""

# Complete these functions only

def compare(a, b, key="studentNumber", descend=False):
    return False

def favSort(data, **kwargs):
    # Replace by your insertionSort or selectionSort algorithm;
    # you will need to make a minor modification so that
    # the kwargs are passed to the swap function.
    return data


# DO NOT EDIT any of the code below.

from resource.school import students

def main():
    data = students()
    key = input("Sort key? ")
    d = input("Acsending or descending? [a/d] ")[0].lower() == "d"
    data = favSort(data, key=key, descend=d)
    for s in data:
        print(s)

main()
