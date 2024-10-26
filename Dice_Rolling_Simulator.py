import random

# Dice Rolling Simulator
def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    num_dice = int(input("Enter the number of dice you want to roll: "))
    
    while True:
        print("\nPress 'R' to roll the dice or 'Q' to quit.")
        choice = input().lower()
        
        if choice == 'r':
            dice_results = [random.randint(1, 6) for _ in range(num_dice)]
            total_sum = sum(dice_results)
            
            print("Rolling the dice...")
            for index, result in enumerate(dice_results, start=1):
                print(f"Dice {index}: {result}")
            
            print(f"Total sum: {total_sum}")
        
        elif choice == 'q':
            print("Thanks for using the Dice Rolling Simulator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please press 'R' to roll or 'Q' to quit.")

if __name__ == "__main__":
    dice_rolling_simulator()
