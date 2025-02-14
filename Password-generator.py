import random

Anzahl = input("Hello. Please type the amount of characters you want in your password: ")

try:
    Anzahl = int(Anzahl)
    if Anzahl > 0:
        Zahl = input("Do you want to include numbers in your password? (y/n) ").lower()
        if Zahl == "y":
            choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            Sonderzeichen = input("Do you want to include special characters in your password? (y/n) ")
            if Sonderzeichen == "y":
                choices += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            elif Sonderzeichen == "n":
                pass 
        elif Zahl == "n":
            choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Sonderzeichen = input("Do you want to include special characters in your password? (y/n) ")
            if Sonderzeichen == "y":
                choices += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            elif Sonderzeichen == "n":
                pass 
        else:
            print("Invalid choice. Please choose y or n.")
            exit()

        password = ''.join(random.choices(choices, k=Anzahl))
        print(f"Generated password: {password}")
    else:
        print("Invalid input. Please type a number above 0.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
