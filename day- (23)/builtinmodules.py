import random
import string
name=input().title()
dob=int(input())
characters = name + str(dob) +"!","@","#","$","%","^","&","*"
password = "".join(random.choices(characters))
print("Generated password:", password)
