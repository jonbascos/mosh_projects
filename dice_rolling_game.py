import random

print("Welcome to the Dice Rolling Game")

roll_dice = input("Would you like to roll the dice (y/n) ? ").lower()

while roll_dice != 'n':
    
    if roll_dice != 'y':
        print("Invalid choice!")
        roll_dice = input("Would you like to roll the dice (y/n) ? ").lower()
    else:
        dice_value = [1, 2, 3, 4, 5, 6]
        dice1 = random.choice(dice_value)
        dice2 = random.choice(dice_value)
        
        print(f'({dice1}, {dice2})')
        
        roll_dice = input("Would you like to roll the dice (y/n) ? ").lower()
