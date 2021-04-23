import string
import random

print("Welcome to the PyPassword Generator!")

# check whether the user is inputting an int, re-prompting if necessary
while True:
    try: 
        length = int(input("\nEnter the length of your password: "))
        break

    except ValueError:
        print("Please enter a number")

# create a string of upper, lower, digits, and symbols to sample from
characters = string.ascii_letters + string.digits + string.punctuation

# temporary variable to randomly sample the string for password characters
temp = random.sample(characters, length)

# join the characters together as a password and print it
password = "".join(temp)

print(password)