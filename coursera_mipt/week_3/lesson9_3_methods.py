"""
property allows us to modify private _power variable
setter allows to check if value is positive in this case

"""


class Robot:
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power


# here we checked if value < 0 then do self._power = 0

android = Robot(100)
android.power = -20
print(android.power)
