"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 8
"""

class Point2D:
    "A class to represent a point in a 2D plane"

    def __init__ (self, x, y):
        self._x = x
        self._y = y

    def __sub__ (self, other):
        """Subtract two points and return the
           answer as a new Point2D instance..."""

        x = self._x - other._x
        y = self._y - other._y
        return Point2D(x, y)

    def coords (self):
        return self._x, self._y

    def __str__ (self):
        return str(self.coords())


# Main program...
p1 = Point2D(8.0, 5.2)
p2 = Point2D(3.0, -1.0)
print(p2 - p1)           # (-5.0, -6.2)