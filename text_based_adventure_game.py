# Text-based Adventure Game
def text_adventure_game():
    print("Welcome to the Text-based Adventure Game!")
    player_name = input("Enter your name: ")
    
    print(f"\nHello, {player_name}! You find yourself in a mysterious castle with multiple paths.")
    print("Your goal is to navigate through the castle and find the hidden treasure.")
    print("Be careful, as there may be dangers and traps along the way!")
    
    while True:
        print("\nChoose your path:")
        print("1. Go left")
        print("2. Go right")
        print("3. Go straight")
        print("4. Quit the game")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print("\nYou chose to go left. You enter a dark hallway.")
            print("You hear strange noises, but you find a torch to light your way.")
            print("Suddenly, a ghost appears! You run back to the starting point.")
        
        elif choice == "2":
            print("\nYou chose to go right. You enter a room filled with treasures.")
            print("However, the room is guarded by a fierce dragon!")
            print("You try to sneak past the dragon, but it spots you. You run away in fear.")
        
        elif choice == "3":
            print("\nYou chose to go straight. You find a hidden passage.")
            print("As you walk through the passage, you come across a riddle.")
            print("Solve the riddle to proceed: What has keys but can't open locks?")
            answer = input("Enter your answer: ").lower()
            
            if answer == "keyboard":
                print("\nCongratulations! You solved the riddle and find the hidden treasure!")
                print("You have successfully completed the adventure.")
            else:
                print("\nSorry, that's not the correct answer. The passage leads to a dead end.")
        
        elif choice == "4":
            print("\nYou decided to quit the game. Thank you for playing!")
            break
        
        else:
            print("\nInvalid choice. Please enter a valid option.")

if __name__ == "__main__":
    text_adventure_game()
