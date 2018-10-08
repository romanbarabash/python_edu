
# print key value

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    print(key, d[key])

# inventory

inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
             'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
             'burlap bag': ['apple', 'small ruby', 'three-toed sloth']}

# Adding a key 'burlap bag' and assigning a list to it

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
gold_new = inventory['gold'] + 50
inventory['gold'] = gold_new
