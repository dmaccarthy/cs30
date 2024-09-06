"""
CSE 3110: Iterative Algorithms
Linear Search
"""

# Complete these functions only...

def search(data, criteria, **kwargs):
    "Linear search algorithm"
    yield "Not implemented!"

def matchYear(record, year):
    "Check whether record birthday matches year"
    return True

def matchSurname(record, name):
    "Check whether record matches surname"
    return True


# DO NOT EDIT any of the code below except to
# comment / uncomment lines 29 and 30.

from resource.school import students

def main():
    data = students()
    print("Searching:")
    #   for match in search(data, matchSurname, name="Smith"):
    for match in search(data, matchYear, year=2004):
        print(match)

main()
