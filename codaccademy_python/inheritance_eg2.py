"""
The first argument passed to __init__() must always be the keyword self -
this is how the object keeps track of itself internally - but we can pass additional variables after that.
In order to assign a variable to the class (creating a member variable), we use dot notation.
For instance, if we passed newVariable into our class, inside the __init__() function we would say:
self.new_variable = new_variable

"""


class Employee(object):

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):

    # override
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        # supper usage
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))
