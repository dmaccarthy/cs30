"""
CSE 3120: Object-Oriented Programming 1
Modifiers & Accessors
"""

# Complete this class definition only

class Point2D:
    "A class for representing points in a 2D plane"


# DO NOT EDIT any of the code below except
# for the coordinates of the two points.

def main():
    p1 = Point2D()
    p1.setCoords(4.0, -1.5)
    p2 = Point2D()
    p2.setCoords(8.0, 1.5)

    print(p1.distance(p2))           # 5.0
    print(p1.slope(p2))              # 0.75
    print(p1.midpoint(p2).coords())  # (6.0, 0.0)


main()
