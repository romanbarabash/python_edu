import random

random_set = set()

while True:
    new_random = random.randint(1, 10)
    new_number = random.randint(1, 10)
    if new_number in random_set:
        break

    random_set.add(new_number)

print(len(random_set) + 1)


