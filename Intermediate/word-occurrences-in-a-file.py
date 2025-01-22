filename = input("Enter filename: ")
with open(filename, 'r') as file:
    text = file.read()

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word occurrences:", word_count)
