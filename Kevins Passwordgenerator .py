import random

while True:
    x = input("Please type password: ")

    if x == 'password':
        random_number = random.randint(1000000, 9999999)
        print(f"Your new password is: {random_number}")
        break
    else:
        print("Please type password, and not something else!")
