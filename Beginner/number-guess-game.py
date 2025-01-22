import random

random_number = random.randint(1, 10)
guess = 0

while guess != random_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")

print("You guessed it!")
