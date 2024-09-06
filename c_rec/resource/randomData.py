from random import randint

def randomData(n=1000, maxNum=100):
	"Make a list of random numbers"
	return [randint(0, maxNum) for i in range(n)]

def ascend(a, b):
    "Check order of a and b"
    return 0 if a == b else 1 if a < b else -1
