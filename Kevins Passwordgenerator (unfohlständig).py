import random

# 5 stellige zahl zufällig generieren
x = input("Please type the number one for your new password: ")
if x == '1':
    random_number = random.randint(10000, 99999)
    print(f"Your new password is: {random_number}")
