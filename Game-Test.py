import random
player_point = 0 
com1_point = 0
com2_point = 0 
com3_point = 0

choices = ["1", "2", "3"]
computer_choice = random.choice(choices)
computer_choice2 = random.choice(choices)
computer_choice3 = random.choice(choices)
counter = 0

while True:
    player_choice = input(f"Current number {counter}. Choose between 1, 2, or 3: ")
    if player_choice in choices:
        counter += int(player_choice)
        if counter >= 11:
            print("You lose")
            com2_point += 1
            counter = 0
            continue 
        print(counter)
        counter += int(computer_choice)
        if counter >= 11:
            print("Computer1 lost")
            com1_point += 1 
            counter = 0
            continue
        print(counter)
        counter += int(computer_choice2)
        if counter >= 11:
            print("Computer2 lost")
            player_point += 1
            counter = 0
            continue
        print(counter)
        counter += int(computer_choice3)
        if counter >= 11:
            print("Computer3 lost")
            com3_point += 1
            counter = 0
            continue
        print(counter)
    elif player_choice== "q":
        print(f"Score: You {player_point} - {com1_point} Computer1 - {com2_point} Computer2 - {com3_point} Computer3")
        exit()
            
    else:
        print("Invalid choice. Please choose between 1, 2, or 3.") 
        continue

    print(f"Score: You {player_point} - {com1_point} Computer1 - {com2_point} Computer2 - {com3_point} Computer3")