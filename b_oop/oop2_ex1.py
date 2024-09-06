"""
CSE 3120: Object-Oriented Programming 1
Modifiers & Accessors — Example 1
"""

class Temperature:
    "A class for representing temperature data"

    def setCelsius (self, degC=0.0):
        "Set the temperature value in °C"
        self._degC = degC

    def setKelvin (self, degK=0.0):
        "Set the temperature value in Kelvins"
        self._degC = degK - 273.15

    def setFahrenheit (self, degF=0.0):
        "Set the temperature value in °F"
        self._degC = (degF - 32.0) / 1.8

    def Celsius (self):
        "Return the temperature value in °C"
        return self._degC

    def Kelvin (self):
        "Return the temperature value in Kelvins"
        return self._degC + 273.15

    def Fahrenheit (self):
        "Return the temperature value in °F"
        return self._degC * 1.8 + 32.0


# Main program...

temp = Temperature()        # Create a Temperature instance
temp.setCelsius(20.0)       # Set the temperature to 20.0 °C
print(temp.Fahrenheit())    # 68.0
