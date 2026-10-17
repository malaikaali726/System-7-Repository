# Task 2: Number guessing game
import random

def guessing_game():
    print("Number Guessing Game")
    print("I am thinking of a number between 1 and 100.\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a number.\n")
            continue

        attempts += 1

        if guess < secret:
            print("Too low.\n")
        elif guess > secret:
            print("Too high.\n")
        else:
            print(f"Correct! The number was {secret}. You won in {attempts} attempts.")
            break

if __name__ == "__main__":
    while True:
        guessing_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Game over. Thank you!")
            break