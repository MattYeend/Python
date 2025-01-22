string = input("Enter a string: ")
frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:", frequency)
