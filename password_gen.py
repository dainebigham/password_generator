import string
import random
import os

print("Welcome to the PyPassword Generator!")

# check whether the user is inputting an int, re-prompting if necessary
while True:
    try: 
        length = int(input("\nEnter the length of your password: "))
        break

    except ValueError:
        # clear the screen before print out error
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the PyPassword Generator!\n(Please enter a number)")
        

# create a string of upper, lower, digits, and symbols to sample from
characters = string.ascii_letters + string.digits + string.punctuation

# temporary variable to randomly sample the string for password characters
temp = random.sample(characters, length)

# join the characters together as a password and print it
password = "".join(temp)

print(password)