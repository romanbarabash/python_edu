import random

number = random.randint(0, 101)

while True:

    answer = input("Set number: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Set correct answer: ")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Guessing number is lower: ")
    elif user_answer < number:
        print("Guessing number is bigger: ")
    else:
        print("Exact number!: ")
        break



