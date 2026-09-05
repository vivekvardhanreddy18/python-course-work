import random
name=input()
dob = int(input())
pw = random.choice([name, str(dob)]) + random.choice(["@","#","$","&*", "A","b",str(dob)])
print(pw)
