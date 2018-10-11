# define string id

example_string = "Hello"
print(example_string)
print(id(example_string))

example_string += ", world"
print(example_string)
print(id(example_string))


# string slicing
# [start:stop:step]

example_string1 = "Python course on course"
print(example_string1[7:])
print(example_string1[7:13])

# METHODS

# count - return number of symbols counted
quote = """Hi my name is python and i am not a reptile"""
print(quote.count("a"))

# encode - return an encoded version of the string as a bytes object.
print(quote.encode())

# find - the lowest index in the string where substring sub
print(quote.find("python"))

# verify if str exists in another string
if_exists = "python" in quote
print(if_exists)

# verify if string is digit
print(quote.isdigit())

# convert int to string
num_string = str(999.01)
print(type(num_string))

# check if string is not NULL
print(bool(num_string))

# INPUT

# input get and store
# name = input("Set your name: ")
# print(name)


# NONE OBJECT

answ = None
print(type(answ))

income = None

# usage example

if income is None:
    print("Not started selling")
elif not income:
    print("No sells yet")










