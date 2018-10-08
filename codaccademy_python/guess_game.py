from random import randint
from Tools.scripts.treesync import raw_input

random_number = randint(1, 10)
guesses_left = 3

# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if random_number == guess:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")
