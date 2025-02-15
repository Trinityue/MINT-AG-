import random
player_point = 0 
com1_point = 0
com2_point = 0 
com3_point = 0
com4_point = 0

choices = ["1", "2", "3"]
computer_choice = random.choice(choices)
computer_choice2 = random.choice(choices)
computer_choice3 = random.choice(choices)
computer_choice4 = random.choice(choices) 
counter = 0
while True:
    x = input ("how many coms do you want? (1-4)")
    if x not in ["1", "2", "3", "4"]:
        print ("Invalid choice. Please choose between 1, 2, 3, or 4.")
        continue
<<<<<<< HEAD:Game-Test.py
    elif x == "1":
        while True:
            player_choice = input(f"Current number {counter}. Choose between 1, 2, or 3: (Type q to quit ; Type r or rules to read the rules)")
            if player_choice in choices:
                counter += int(player_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("You lose")
                    com2_point += 1
                    counter = 0
                    continue 
                print(f"You: {counter}")
                counter += int(computer_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer1 lost")
                    com1_point += 1 
                    counter = 0
                    continue
                print(f"Com1: {counter}")	
            elif player_choice== "q":
                print(f"Score: You - {player_point}  Com1 - {com1_point} Com2 - {com2_point} Com3 - {com3_point}")
                exit()
            elif player_choice == "rules" or player_choice == "r":
                print ("The rules are simple. You and the computer take turns to choose a value between 1 and 3.The value will be added to a counter. The first one who makes the counter above 11 loses. Good luck!")
                
            else:
                print("Invalid choice. Please choose between 1, 2, or 3.") 
                continue
    elif x == "2":
        while True:
            player_choice = input(f"Current number {counter}. Choose between 1, 2, or 3: (Type q to quit ; Type r or rules to read the rules)")
            if player_choice in choices:
                counter += int(player_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("You lose")
                    com2_point += 1
                    counter = 0
                    continue 
                print(f"You: {counter}")
                counter += int(computer_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer1 lost")
                    com1_point += 1 
                    counter = 0
                    continue
                print(f"Com1: {counter}")
                counter += int(computer_choice2)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer2 lost")
                    player_point += 1
                    counter = 0
                    continue
                print(f"Com2: {counter}")
            elif player_choice== "q":
                print(f"Score: You - {player_point}  Com1 - {com1_point} Com2 - {com2_point} Com3 - {com3_point}")
                exit()
            elif player_choice == "rules" or player_choice == "r":
                print ("The rules are simple. You and the computer take turns to choose a value between 1 and 3.The value will be added to a counter. The first one who makes the counter above 11 loses. Good luck!")
                
            else:
                print("Invalid choice. Please choose between 1, 2, or 3.") 
                continue
    elif x == "3":
        while True:
            player_choice = input(f"Current number {counter}. Choose between 1, 2, or 3: (Type q to quit ; Type r or rules to read the rules)")
            if player_choice in choices:
                counter += int(player_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("You lose")
                    com2_point += 1
                    counter = 0
                    continue 
                print(f"You: {counter}")
                counter += int(computer_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer1 lost")
                    com1_point += 1 
                    counter = 0
                    continue
                print(f"Com1: {counter}")
                counter += int(computer_choice2)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer2 lost")
                    player_point += 1
                    counter = 0
                    continue
                print(f"Com2: {counter}")
                counter += int(computer_choice3)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer3 lost")
                    player_point += 1
                    counter = 0
                    continue
                print(f"Com3: {counter}")
            elif player_choice== "q":
                print(f"Score: You - {player_point}  Com1 - {com1_point} Com2 - {com2_point} Com3 - {com3_point}")
                exit()
            elif player_choice == "rules" or player_choice == "r":
                print ("The rules are simple. You and the computer take turns to choose a value between 1 and 3.The value will be added to a counter. The first one who makes the counter above 11 loses. Good luck!")
                
            else:
                print("Invalid choice. Please choose between 1, 2, or 3.") 
                continue
    elif x == "4":
        while True:
            player_choice = input(f"Current number {counter}. Choose between 1, 2, or 3: (Type q to quit ; Type r or rules to read the rules)")
            if player_choice in choices:
                counter += int(player_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("You lose")
                    com2_point += 1
                    counter = 0
                    continue 
                print(f"You: {counter}")
                counter += int(computer_choice)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer1 lost")
                    com1_point += 1 
                    counter = 0
                    continue
                print(f"Com1: {counter}")
                counter += int(computer_choice2)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer2 lost")
                    player_point += 1
                    counter = 0
                    continue
                print(f"Com2: {counter}")
                counter += int(computer_choice3)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer3 lost")
                    player_point += 1
                    counter = 0
                    continue
                print(f"Com3: {counter}")
                counter += int(computer_choice4)
                if counter >= 11:
                    print (f"{counter} > 11")
                    print("Computer4 lost")
                    player_point += 1
                    counter = 0
                    continue
                print(f"Com4: {counter}")
            elif player_choice== "q":
                print(f"Score: You - {player_point}  Com1 - {com1_point} Com2 - {com2_point} Com3 - {com3_point} Com4 - {com4_point}")
                exit()
            elif player_choice == "rules" or player_choice == "r":
                print ("The rules are simple. You and the computer take turns to choose a value between 1 and 3.The value will be added to a counter. The first one who makes the counter above 11 loses. Good luck!")
                
            else:
                print("Invalid choice. Please choose between 1, 2, or 3.") 
                continue
=======

    #print(f"Score: You {player_point} - Com1 {com1_point} Com2 - {com2_point} Com3 - {com3_point}") 
>>>>>>> 33febf90060b369e67ac59971b745fb38da05164:Elf-Raus.py
