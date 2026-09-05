import random
import string
name=input().title()
dob=int(input())
characters = ["!","@","#","$","%","^","&","*"]
password = name + (random.choice(characters)) + str(dob)
print("Generated password:", password)
