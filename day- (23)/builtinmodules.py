import random
name=input()
dob = int(input())
pw = random.choice([name, str(dob)]) + random.choice(["@#$&*", "!@#$%", "abc123"])
print(pw)
