import random

answer = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        print("Congratulations!  You guessed the number.")
        break