try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)
    print("Division =", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")