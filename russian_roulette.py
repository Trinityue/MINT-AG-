import random
from time import sleep
ende = str 
x  = 0
y = 0 
buletts = int(input("How many bullets do you want to put in the gun? (1 - infinity)"))
hot_bullet = random.randint(1, buletts)
won_games = 0 
com_choice = random.randint(1,2)
print ("Welcome to the Russian Roulette Game. For rules press(R). To start the game press(S)")
while x == 0:
    start = input()
    if start == "R":
        print("placeholder")
    elif start == "S" or "s":
        while y == 0:
            choiche = input("It's your turn. Do you want to shot you (y) or your opponent (o)?[q to quit]")
            if choiche == "q":
                print (f"You won {won_games} games. Goodbye")
                exit()
            sleep (5)
            if choiche == "y" or "o" :
                x += 1 
                if x == hot_bullet and choiche == y:
                    print ("You Lost UwU")
                    break
                elif x == hot_bullet and choiche == "o" :
                    print ("You Won UwU") 
                    won_games += 1
                    ende = input("Do you want to play again? (y/n)")
                    if ende == "y":
                        continue
                    elif ende == "n":
                        print (f"You won {won_games} games. Goodbye")
                        exit() 
                    else :
                        print (f"Invalid input. the game ends.You won: {won_games} games")
                        exit ()
                else: 
                    print ("Nothing happened. It's your opponent's turn")
                    sleep(5)
                    if com_choice == 1 or 2:
                        x += 1 
                        if com_choice == 1:
                            print ("Your opponent shot himself")
                            sleep (5)
                            if x == hot_bullet and com_choice == 1:
                                print ("You Won UwU")
                                won_games += 1
                                continue 
                        elif x == hot_bullet and com_choice == 2:
                            print ("You Lost UwU")
                            break 
                        elif com_choice == 2:
                            print ("Your opponent shot you")
                            sleep (5)
                            if x == hot_bullet and com_choice == 1:
                                print ("You Won UwU")
                                won_games += 1
                                continue
                        elif x == hot_bullet and com_choice == 2:
                            print ("You Lost UwU")
                            break 
                                
                            

                    


