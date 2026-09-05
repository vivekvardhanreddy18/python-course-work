import random
import string

characters = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(random.choices(characters, k=12))
print("Generated password:", password)
