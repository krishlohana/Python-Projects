# Password Generator

import random
import string

lower = string.ascii_lowercase

upper = string.ascii_uppercase

numbers = string.digits

symbols = string.punctuation

characters = lower + upper + numbers + symbols

length = int(input("Enter the desired length of the password: "))

if length <= 0:
    print("Length must be a positive integer....")

Generate_Password = "".join(random.choice(characters) for _ in range(length))

print("Your Password Is: " , Generate_Password)
