class Robot:

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    # var which belongs to class (class level variable)
    count = 0


""" 
 __init__ takes as 1st argument link to the class object (not initialized yet)
 and then takes class arguments (which is manufacturer)
  self.manufacturer = manufacturer, means that we set attribute of class example to manufacturer argument
  since that time we can call name of class object (robot.manufacturer)
 
"""

# created class object
robot = Robot("BDyn")
print(robot.manufacturer)

# set another manufacturer to robot object
robot.manufacturer = "Apple"
print(robot.manufacturer)

# below code throw an error after del attribute manufacturer
# del robot.manufacturer
# print(robot.manufacturer)


# __dict__ method returns all attributes and its values as dict
robot.mass = 152
print(robot.__dict__)
