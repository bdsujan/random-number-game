import random

# Generate a random number between 1 and 100
number: int = random.randint(1, 100)

# Inform the user about the game
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Variable to track if the number has been guessed
guessed = False

# Loop until the user guesses correctly
while not guessed:
    try:
        guess = int(input("Enter your guess: "))

        # Provide feedback if the guess is too high or too low
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print(f"Correct! The number was {number}.")
            guessed = True
    except ValueError:
        print("Please enter a valid number.")
