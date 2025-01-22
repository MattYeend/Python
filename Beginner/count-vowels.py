string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)

print(f"Number of vowels: {count}")