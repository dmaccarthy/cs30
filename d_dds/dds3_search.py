"""
CSE 3320: Dynamics Data Structures 1
Searching & Sorting - Question 1a
"""

# Duplicate your ListNode and LinkedList classes
# from dds2_ll.py. Make all required changes.


# DO NOT EDIT any of the code below
# except to change the search criteria.

from resource.student import Student

# Randomly generate data for 1200 students
students = LinkedList()
students.insert(Student() for i in range(1200))

# Search criteria
crit = {"birthyear":1999, "courses":["Computing Science 30"]}

# Perform search
for student in students.find(match, 20, **crit):
    print(student.data)
