empty_set = set()
odd_set = set()
even_set = set()

# stores only unique set of elements
number_set = {1, 2, 3, 3, 4, 5}
print(number_set)

# add elements into set with for iteration, odd and even
for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set)
print(even_set)

# union of sets
union_set = odd_set.union(even_set)
print(union_set)

# difference set
difference_set = odd_set.difference(even_set)
print(difference_set)

# remove element
even_set.remove(2)
print(even_set)

# frozen set, cannot add or delete elements
frozen = frozenset(['Anna', 'Elsa', 'Jurgen'])
frozen.add('Olaf') # this results error

