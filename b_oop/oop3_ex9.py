"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 9
"""

class Color:
    "A class to represent RGB color data"

    def __init__ (self, name, r, g, b):
        self._name = name
        self._rgb = r, g, b

    def __iter__ (self):
        colors = "Red", "Green", "Blue"
        for i in range(3):
            yield colors[i], self._rgb[i]
        yield "Name", self._name


# Main program...
c1 = Color("Violet", 139, 0, 255)
print(dict(c1))