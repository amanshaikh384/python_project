import random

# Number Guessing Game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Guess the secret number (between 1 and 100): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        attempts += 1
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
