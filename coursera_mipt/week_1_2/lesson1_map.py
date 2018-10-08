# create empty map
empty_dict = {}
empty_dict = dict()

beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar',
}

# add new element into the map
beatles_map['Ringo'] = 'Drums'

# del element from the map
del beatles_map['John']
print(beatles_map)

# also add (update)
beatles_map.update({'John': 'Guitar'})
print(beatles_map)

# also delete element
beatles_map.pop('Ringo')
print(beatles_map)

# add def key : value
empty_dict.setdefault('Slim Shady', 'Micro')
print(empty_dict)

# iterating by keys
for key in beatles_map:
    print(key)

# iterating by keys, values
for key, value in beatles_map.items():
    print('{}: {}'.format(key, value))

# iterating by values
for value in beatles_map.values():
    print(value)
