"""
The first argument passed to __init__() must always be the keyword self -
this is how the object keeps track of itself internally - but we can pass additional variables after that.
In order to assign a variable to the class (creating a member variable), we use dot notation.
For instance, if we passed newVariable into our class, inside the __init__() function we would say:
self.new_variable = new_variable

"""


class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


my_triangle = Triangle(30, 60, 30)
print(my_triangle.check_angles())


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


my_equilateral = Equilateral()
print(my_equilateral.check_angles())
