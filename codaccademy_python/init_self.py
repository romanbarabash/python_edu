"""
The first argument passed to __init__() must always be the keyword self -
this is how the object keeps track of itself internally - but we can pass additional variables after that.
In order to assign a variable to the class (creating a member variable), we use dot notation.
For instance, if we passed newVariable into our class, inside the __init__() function we would say:
self.new_variable = new_variable

"""


# __repr__()

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point)
