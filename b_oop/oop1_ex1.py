"""
CSE 3120: Object-Oriented Programming 1
Objects — Example 1
"""

from datetime import date

today = date.today()
newYear = date(2021, 1, 1)
confed = date(1867, 7, 1)
print(today, newYear, confed, sep="\n")
