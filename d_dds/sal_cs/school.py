# Copyright 2025 D.G. MacCarthy <https://github.com/dmaccarthy>
#
# This file is part of "sal_cs".
#
# "sal_cs" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "sal_cs" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "sal_cs".  If not, see <https://www.gnu.org/licenses/>.

from random import randint, uniform
from datetime import date, timedelta
from sal_cs import *

def jan1(today=None):
    if today is None:
        today = date.today()
    year = today.year
    if today.month > 8:
        year += 1
    start = date(year, 1, 1)
    return start

def bday_from_grade(grade, today=None):
    start = jan1(today)
    age = grade + 5
    return start - 365.25 * timedelta(age - 1/12 + uniform(0, 1))

def bday_from_age(age): return date.today() - 365.25 * timedelta(age)

def fdict(args, **kwargs):
    data = {}
    for k, f in kwargs.items():
        try: data[k] = f(**args)
        except: pass
    return data

def student(id=None, grade=None):
    if grade is None:
        grade = randint(10, 12)
    data = {"grade": grade}
    data.update(fdict(data, birthday=bday_from_grade, surname=surname, givenname=givenname))
    if id: data["id"] = id
    return data

def student_list(n=100, id=1001, d=4):
    data = []
    for n in range(n):
        data.append(student(id))
        id += randint(1, d)
    return data

def student_marks(n=None, id=1002):
    if n is None: n = randint(12, 40)
    if id is None: id = randint(300, 1200)
    return list(zip(range(id-1, id+n), (randint(40, 100) for s in range(n))))
