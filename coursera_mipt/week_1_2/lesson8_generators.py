"""
yield allows us to return result of the function on yield keyword,
but without finish like happens on return keyword.
On the example below, current returns/yields each time we are iterating over even_range


"""


def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


for number in even_range(0, 10):
    print(number)

print()

"""
On the example below, 1st iteration completes after yield item code.
we got print statement 2nd time when we iterate over 2nd element (get yield 2nd time then)  

"""


def list_generator(list_obj):
    for item in list_obj:
        yield item
        print("After yielding {}", format(item))


generator = list_generator([1, 2])

print(next(generator))
print(next(generator))

print()

"""
On the example below, func returns/yields each fibonacci number and then make operations with them

"""


def fibonacci(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)


