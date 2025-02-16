import random

player_score = 0
computer_score = 0

while True:
    x = input("Hello. Let's play. Choose between rock, paper, or scissors.(r/p/s) or 'q' to quit: ")

    if x == 'q':
        break

    if x in ["r", "p", "s"]:
        choices = ["r", "p", "s"]
        computer_choice = random.choice(choices)
        print("I choose", computer_choice)

        if x == computer_choice:
            print("It's a tie!")
        elif (x == "r" and computer_choice == "s") or (x == "p" and computer_choice == "r") or (x == "s" and computer_choice == "p") or (x == 69):
            print("You win this round!")
            player_score += 1
        else:
            print("I win this round!")
            computer_score += 1

        print(f"Score: You {player_score} - {computer_score} Computer")
    elif x == "69": 
        print ("Nice, but that's not what I came here for in the first place")
    else:
        print("Invalid choice. Please choose r, p, or s.")

print(f"Final Score: You {player_score} - {computer_score} Computer")
print("Thanks for playing!")
