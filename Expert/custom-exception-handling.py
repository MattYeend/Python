class NegativeNumberError(Exception):
    pass

number = int(input("Enter a number: "))
if number < 0:
    raise NegativeNumberError("Negative numbers are not allowed.")
else:
    print("You entered:", number)
