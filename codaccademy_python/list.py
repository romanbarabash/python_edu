
# multiply the second element of the list by 5, overwrite the second element with that result.
n = [1, 3, 5]
a = n[1] * 5
n[1] = a

# add '4' to the list
n.append(4)

# remove the 1st item from the list
del (n[0])

# create a function called flatten that takes a single list and /
# concatenates all the sublists that are part of it into a single list

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists):
    results = []
    for numbers in lists:
        for var in numbers:
            results.append(var)
    return results


# list comprehension
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print(cubes_by_four)

# list reverse
my_list = range(1, 11)

backwards = my_list[::-1]
print(backwards)
