"""
CSE 3320: Dynamics Data Structures 1
Searching & Sorting - Question 1b
"""

# Duplicate your ListNode and LinkedList classes
# from dds3_search.py. Make all required changes.


# DO NOT EDIT any of the code below
# except to change the 'recursive' varaible.

from resource.student import Student

# Randomly generate data for 1200 students
students = LinkedList()
students.insert(Student() for i in range(1200))

# Sort
recursive = False
if recursive:
    students.mSort(compareBirthday)
else:
    students.iSort(compareBirthday)

# Print results
for student in students:
    print(student.data)
