
# lambda variable expression

"""
Only we don't need to actually give the function a name; it does its work and returns a value without one.
That's why the function the lambda creates is anonymous function.

"""

languages = ["HTML", "JavaScript", "Python", "Ruby"]

result1 = list(filter(lambda x: x is "Python", languages))
print(result1)

# Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).

squares = [x ** 2 for x in range(1, 11)]
result2 = list(filter(lambda x: 30 <= x <= 70, squares))
print(result2)

# parse message
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = ''.join(filter(lambda x: x != 'X', garbled))
print(message)
