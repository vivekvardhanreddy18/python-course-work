import random
import string

name = input("Enter your name: ").strip().replace(" ", "")
dob = input("Enter your date of birth: ").strip()

password = list(name + dob)
password += [
	random.choice(string.ascii_uppercase),
	random.choice(string.ascii_lowercase),
	random.choice(string.digits),
	random.choice("!@#$%^&*"),
]
password += random.choices(
	string.ascii_letters + string.digits + "!@#$%^&*", k=4
)
random.shuffle(password)
print("Generated password:", "".join(password))
