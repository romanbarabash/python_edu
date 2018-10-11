"""
static method creation example

"""


class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


@staticmethod
def is_age_valid(age):
    return 0 < age < 150


print(Human.is_age_valid(35))
