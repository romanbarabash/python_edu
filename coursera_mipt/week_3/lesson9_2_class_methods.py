"""
public methods	      Accessible from anywhere
private methods	      Accessible only in their own class. starts with two underscores
public variables      Accessible from anywhere
private variables     Accessible only in their own class or by a method if defined. starts with two underscores
"""


class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    # __ meant __say method is private
    def __say(self, text):
        print(text)

    def say_name(self):
        self.__say("Hello, I am {self._name}")

    def say_how_old(self):
        self.__say("I am {self._age} years old")


rob = Human("Bob", age=29)
rob.say_name()
rob.say_how_old()
