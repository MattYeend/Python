import random
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=length))

print("Generated password:", password)
