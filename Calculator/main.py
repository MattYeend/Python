# Potential to comment out
import sys
import os

# Add the parent directory of "Python" to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# Potential to comment out above

from Python.Calculator.operations.addition import add
from Python.Calculator.operations.subtraction import subtract
from Python.Calculator.operations.multiplication import multiply
from Python.Calculator.operations.division import divide

def main():
    print("Welcome to the Basic Calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nChoose an operation (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Invalid choice. Please select a valid operation.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
