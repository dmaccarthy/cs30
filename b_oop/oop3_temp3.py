"""
CSE 3120: Object-Oriented Programming 1
Special Methods
"""

# Copy your Temperatue class from oop3_temp2.py
# here and then make the required changes.

class Temperature:
    ""

# DO NOT EDIT any of the code below
# except to change the temperature value.

def main():
    t = Temperature(K=0.0)
    for unit in t:
        print(unit)

main()

# Expected program output...
# ('Celsius', -273.15)
# ('Kelvin', 0.0)
# ('Fahrenheit', -459.67)