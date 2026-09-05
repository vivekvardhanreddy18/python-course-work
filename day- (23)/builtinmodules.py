import random
import string
name=input()
dob=int(input())
characters = string.name + string.dob + "!@#$%^&*"
password = "".join(random.choices(characters, k=12))
print("Generated password:", password)
