marks = (float(input("Enter Your Mark: ")))
if 100 >= marks >= 90:
    result = "Pass with  A+"
elif  89 >= marks >= 80:
    result = "Pass with A"
elif  79 >= marks >= 70:
    result = "Pass with B"
elif  69 >= marks >= 60:
    result = "Pass with C"
else:
    result = "Fail"

print(result)