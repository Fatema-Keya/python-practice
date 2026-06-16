a = (float(input("Enter your mark1: ")))
b = (float(input("Enter your mark2: ")))
c = (float(input("Enter your mark3: ")))
d = (float(input("Enter your mark4: ")))

total = a + b + c + d
avg = (a + b + c + d) / 4

if avg>=  40:
    result =  "pass"
else:
    result =  "Fail"


print("Total: ", total)
print("Avarage: ", avg)
print("Result: ", result)
