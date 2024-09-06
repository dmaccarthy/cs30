"""
CSE 3310: Recursive Programming
Recursion
"""


# Complete this function only...

def moveDisks(towers, n, towerFrom, towerTo):
    pass


# DO NOT EDIT any of the code below.

def output(towers):
    "Print the state of the disks/towers"
    print("{:5d} > {}".format(towers[0], towers[1:]))

def main():
    n = int(input("How many disks? "))
    towers = [0, list(range(n, 0, -1)), [], []]
    output(towers)
    moveDisks(towers, n, 1, 2)

main()