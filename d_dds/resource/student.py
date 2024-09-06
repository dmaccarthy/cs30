from random import randint
from datetime import date, timedelta

class Student:
    _count = 0
    _avg12 = date(2005, 2, 1)
    _courseList = ["Computing Science {}", "Science {}", "Mathematics {}-1",
        "English {}-1", "Social Studies {}-1", "Phys Ed {}", "Drama {}", "Art {}"]

    def __init__(self):
        Student._count += 1
        self.id = 1000000 + Student._count
        self.grade = randint(10, 12)
        self._bday = randint(-200, 200)
        self._courses = set([randint(0, len(self._courseList)-1) for i in range(4)])

    @property
    def birthday(self):
        bday = self._avg12 + timedelta(days=self._bday + 365 * (12 - self.grade))
        return [bday.year, bday.month, bday.day]

    @property
    def courses(self):
        n = 10 * self.grade - 90 
        return [self._courseList[i].format(n) for i in sorted(self._courses)]

    @property
    def info(self):
        return dict(id=self.id, grade=self.grade, birthday=self.birthday, courses=self.courses)

    def __str__(self):
        return "Student[{}]".format(self.info)
