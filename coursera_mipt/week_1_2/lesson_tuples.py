# TUPLE (unchangeable collection)

# ordered, unchangeable set of objects
# like a lists but unchangeable
# has hashes
# has built in methods / functions

# can be defined in 2 ways:
empty_tuple = ()
empty_tuple = tuple()

empty_tuple = (int, str, tuple)
print(empty_tuple)

# lists inside tuples can be append
blink_tuple = ([], [])
blink_tuple[0].append(0)
print(blink_tuple)

# can be used as dictionary keys with hash function
# hash(blink_tuple())

