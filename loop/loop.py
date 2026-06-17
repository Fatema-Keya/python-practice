#Print numbers 1–100 using for
for num in range(1,101):
    print(num)

#Print numbers 1–100 using for
for num in range(1,101):
    if num % 2 == 0:
        print(num)
#Sum all numbers from 1 to 50
sum = 0
for i in range(1, 51):
    sum = sum + i

print("total: ",sum)

#Multiplication table
mul = int(input("Enter your Number: "))
for i in range(1,11):
    print(mul,"*",i,"=", mul*i)

