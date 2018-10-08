"""
Functions can be set as func params. eg below

"""


def caller(func, params):
    return func(*params)


def printer(name, origin):
    print("I\'m {} of {}!".format(name, origin))


caller(printer, ["Moana", "Motunui"])

"""
Functions can be set inside another func

"""


def get_multiplier(number):
    def inner(a):
        return a * number

    return inner


multiplier_by_2 = get_multiplier(2)
multiplier_by_2(10)

print(multiplier_by_2.__name__)

"""
Built in functions. Map applies function with the range iteration. eg below,
output: [0, 1, 4, 9, 16]

"""


def squarify(a):
    return a ** 2


print(list(map(squarify, range(5))))

"""
Built in functions. Filter allows to filter on any var iterable object. eg below,
output: [1, 2]

"""


def is_positive(a):
    return a > 0


positive = (list(filter(is_positive, range(-2, 3))))
print(positive)

"""
Built in functions. Lambda (or annonimus func) allows to define func "in place" without def,
to use function only once.
Our function takes x as parameter and operate x ** 2

"""

squared = list(map(lambda x: x ** 2, range(5)))
print(squared)

""" 
Function which converts int list to str list

"""


def stringify_list(num_list):
    return list(map(str, num_list))


print(stringify_list(range(10)))

""" Listing expressions
output1: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
output1: [0, 2, 4, 6, 8]

"""

square_list = [number ** 2 for number in range(10)]
print(square_list)

even_list = [number for number in range(10) if number % 2 == 0]
print(even_list)

""" Zip function allows to join elements. see eg below of joining 2 lists  """

num_list = range(7)
square_list = [x ** 2 for x in num_list]

print(list(zip(num_list, square_list)))





