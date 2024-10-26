import random

# Hangman Game
def hangman_game():
    print("Welcome to Hangman!")
    
    # List of words for the game
    words = ['python', 'hangman', 'computer', 'programming', 'apple', 'banana', 'elephant', 'rainbow', 'chocolate']
    
    # Select a random word from the list
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6
    
    while True:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        
        if display_word == secret_word:
            print("Congratulations! You guessed the word correctly!")
            break
        
        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The word was '{secret_word}'. Better luck next time!")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

if __name__ == "__main__":
    hangman_game()
