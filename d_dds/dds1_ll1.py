"""
CSE 3320: Dynamics Data Structures 1
Linked Lists — Question 1
"""

# Complete this class definition only

class LinkedList:
    ""


# DO NOT EDIT any of the code below
# except to test the main program.

class ListNode:

    def __init__(self, obj):
        self.data = obj
        self._nextNode = None

    def __str__(self):
        return f"{str(self.data)}"


# Main program...

myList = LinkedList(1, True, "three", 4.0)
print(len(myList))
print(myList.first)
print(myList.last)
