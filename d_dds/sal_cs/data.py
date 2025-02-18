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
from datetime import date
from sal_cs import *

def _record(t):
    if t is float: d = uniform(0, 100)
    elif t is int: d = randint(0, 100)
    elif t is str: d = randstr(12)
    elif t is date: d = date(randint(1967, date.today().year), randint(1, 12), randint(1, 28))
    elif t is dict:
        f = list(FIELDS)
        for n in range(randint(0, 4)):
            i = randint(0, len(f) - 1)
            f.remove(f[i])
        d = {}
        for k, v in f:
            d[k] = _record(v)
    else: d = None
    return d

FIELDS = ("Section", int), ("Count", int), ("Created", date), ("Approved", date), ("Code", str), ("Difficulty", float), ("Rating", float)

def random_data(data_type=int, n=100):
    return [_record(data_type) for n in range(n)]
