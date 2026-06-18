def calculator(a, b, oparation):
    if oparation == "+":
        return a + b
    if oparation == "-":
        return a - b
    if oparation == "*":
        return a * b
    if oparation == "/":
        return a / b

num1 = float(input("Enter your first Number: "))
num2 = float(input("Enter your seconnd Number: "))
op = input("Enter what type of oparation you want: ")

print(calculator(num1,num2,op))
