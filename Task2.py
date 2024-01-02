import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    while True:
        user_guess = input("Enter your guess: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_the_number()
