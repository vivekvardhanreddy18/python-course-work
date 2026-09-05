import random
import string
name=input().title()
dob=int(input())
characters = ["!","@","#","$","%","^","&","*"]
password = name + str(random.choices(characters)) + str(dob)
print("Generated password:", password)
