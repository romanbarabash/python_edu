# one line comment

"""
Many lines comment
"""

# number types

num = 13
print(type(num))
# <class 'int'>

num1 = 150.2
print(type(num1))

num1 = int(num1)
print(num1, type(num1))
# 150 <class 'int'>


# change var places

a = 101
b = 207
print(a, b)

a, b = b, a
print(a, b)

# 101 207
# 207 101

