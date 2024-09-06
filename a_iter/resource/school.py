"Generate random student data"

from random import random, choice, randint
from datetime import date, timedelta
from resource.commonnames import names, surnames

def _randStudent(n):
	surname = choice(surnames)
	given = choice(names)
	age = round(365 * (15 + 4 * random()))
	bd = date.today() - timedelta(days=age)
	return dict(surname=surname, givenName=given,
		studentNumber=1000 + n, birthday=bd, grade=randint(10, 12))

def students(n=200):
	return [_randStudent(i) for i in range(n)]