word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
