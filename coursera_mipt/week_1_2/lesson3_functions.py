"""

Python 3.5 also supports types annotation (x: int) and also returns int here (-> int:)

"""


def add(x: int, y: int) -> int:
    return x + y


print(add(5, 7))
print(add("this still ", "works"))


# in python 3.5, variable's name = object in memory, and this name (link to object) sends into the function
def extender(source_list, extended_list):
    source_list.extend(extended_list)


values = [1, 2, 3]
extender(values, [4, 5, 6])

"""
Link to object in memory goes to extender func which changed object in memory
before extender, object in memory is  [1, 2, 3]
after extender, object in memory is [1, 2, 3, 4, 5, 6]

"""

print(values)

"""
if we go to the memory with object link we will see that object is not changable, then we cannot change this object. 
tuple is unchangable object, see the next example
before replacer, object in memory is "Guido", "31/01"
after replacer, object in memory is "Guido", "31/01"

"""


def replacer(source_tuple, replace_with):
    source_tuple = replace_with


user_info = ("Guido", "31/01")
replacer(user_info, ("Larry", "27/09"))

print(user_info)

"""
We can also add names to arguments to see which argument has which name, and also we may not care about arguments order,
in this case

"""


def say(greeting, name):
    print("{} {}!".format(greeting, name))


say(name="Kitty", greeting="Hello")

"""
We should not change global objects inside func, the next code will throw errors:
UnboundLocalError: local variable 'results' referenced before assignment

"""

results = 0

# def increment():
#     results += 1
#     return results

# print(increment())


"""
We cn assign default values into the func, eg:

"""


def function_default(itarable=None):
    if itarable is None:
        iterable = []


"""
We can use asterix in functions to sent any qty of parameters. on the below eg, we sent a list:

"""


def printer_arg(*args):
    print(type(args))

    for argument in args:
        print(argument)


name_list = ["John", "Bill", "Amy"]
printer_arg(*name_list)


def printer_kwarg(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))


payload = {
    'user_id': 117,
    'user_name': "John"
}

printer_kwarg(**payload)


