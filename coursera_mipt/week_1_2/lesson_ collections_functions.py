import random

# LIST

# ordered, changeable set of objects
# supports indexes
# support iterations
# support built in functions and methods

collection = ['list', 'tuple', 'dict', 'set']

# len
print(len(collection))

# index (last) [-1]
print(collection[-1])

# replace in list
collection[3] = 'frozenset'
print(collection)

# verify smthg in list
print("typle" in collection)

# # print each item in collection and index
# for idx, collection in enumerate(collection):
#     print("#{} {}".format(idx, collection))

# to add elements into the list
collection.append("ordered_dict")
print(collection)

# to add elements into the list end
collection.extend(['ponyset', 'unicorndict'])
print(collection)

# to del element from the list
del collection[4]
print(collection)

# min, max, sum
numbers = [4, 17, 19, 9, 2, 6, 10, 13]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# join (format string)
tag_list = ["python", "course", "coursera"]
print(", ".join(tag_list))

# sort list
numbers1 = []
for item in range(10):
    numbers1.append(random.randint(1, 20))

print(numbers1)

# soft list into another list
print(sorted(numbers1))

# sort the same list w/o creation of new one
numbers1.sort()
print(numbers1)

# sort list in reverse mode
print(sorted(numbers1, reverse=True))
numbers1.sort(reverse=True)
print(numbers1)



