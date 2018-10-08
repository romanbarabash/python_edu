"""
Decorator is function which takes function and also return function.
@decorator also meant construction decorated = decorator(decorated)

"""

"""
When we use decorator at example below, we overrides summator() with realization defined at wrapped() function,
and then summator([1, 2, 3, 4, 5]) will be executed with wrapped() realization. 
calling summator.__name__ proofs this. 

"""


def logger(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('files/log.txt', 'w') as f:
            f.write(str(result))

        return result

    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4, 5])
print(summator.__name__)

with open('files/log.txt', 'r') as f:
    print('log.txt: {}'.format(f.read()))

""" 
Decorators chain. 
decorated = first_decorator(second_decorator(decorated))

output:
Inside first_decorator product
Inside second_decorator product
Finally called this...

"""


def first_decorator(func):
    def wrapped():
        print("Inside first_decorator product")
        return func()

    return wrapped


def second_decorator(func):
    def wrapped():
        print("Inside second_decorator product")
        return func()

    return wrapped


@first_decorator
@second_decorator
def decorated():
    print("Finally called this...")


decorated()
