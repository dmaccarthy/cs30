"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 1
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


temp = Temperature()
temp.setCelsius(20.0)
print(temp.Fahrenheit())
