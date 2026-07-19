from utilities.calculator import add, subtract, multiply, divide
from utilities.converter import (
    kg_to_g,
    g_to_kg,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius
)

print("Calculator Operations")
print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))
print("Multiplication:", multiply(20, 10))
print("Division:", divide(20, 10))

print("\nConverter Operations")
print("5 kg =", kg_to_g(5), "g")
print("2500 g =", g_to_kg(2500), "kg")
print("30°C =", celsius_to_fahrenheit(30), "°F")
print("98.6°F =", fahrenheit_to_celsius(98.6), "°C")