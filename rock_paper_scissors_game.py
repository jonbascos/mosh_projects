import random

print("Let's play some Rock, Paper, or Scissors")


game_options = ("r", "p", "s") 
emojis = {
    "r" : "🪨",
    "s" : "✄",
    "p" : "📃"
}

while True:
    players_choice = input("Rock, Paper, Scissors? (r/p/s) ").lower()
    computer_choice = random.choice(game_options)
    
    if players_choice not in game_options:
        print("Invalid choice!")
        continue
    
    print(f'You chose {emojis[players_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')
    
    if players_choice == computer_choice:
        print("You tied!")
    elif (
        (players_choice == "r" and computer_choice == "s") or
        (players_choice == "s" and computer_choice == "p") or
        (players_choice == "p" and computer_choice == "r")
    ):
        
        print("You win!")
    else:
        print("You lose!")
        
    play_again = input("Would you like to play again? (y/n) ").lower()
    
    if play_again == "n":
        break
    
    