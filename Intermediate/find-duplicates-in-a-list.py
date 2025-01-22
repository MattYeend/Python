numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7]
duplicates = set([x for x in numbers if numbers.count(x) > 1])

print("Duplicates:", duplicates)
