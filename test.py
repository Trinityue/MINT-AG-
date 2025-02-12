from time import sleep

while True: 
    x = input("Type the amount of Money you wanna donate ") 
    try: 
        x = int(x) 
        if x > 0:
            print("Thanks for danating")
            break 
        elif x < 0:
            y = input ("Please type a number above 0")
            y = int(y)
            if y > 0:
                print(" Thanks for danating")
            elif y < 0 :
                print("You are not allowed to donate for the next 24 houers ")
    except:
        print("Don't be a Noah and input a number!")
        continue 
    