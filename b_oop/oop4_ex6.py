"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 6
"""

from random import randint

class Dice:

    @staticmethod
    def roll (dice=1):
        while dice > 0:
            yield randint(1,6)
            dice = dice - 1


# Main program...
for roll in Dice.roll(4):
    print("You rolled a {}!".format(roll))
