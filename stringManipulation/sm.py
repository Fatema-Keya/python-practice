sentence = input("Enter a sentence: ")

# Count words
word_count = len(sentence.split())
print("Word Count:", word_count)

# Convert to uppercase
print("Uppercase:", sentence.upper())

# Convert to lowercase
print("Lowercase:", sentence.lower())

# Reverse string
reverse_string = sentence[::-1]
print("Reversed String:", reverse_string)

# Check palindrome
# (Ignore spaces and case)
check = sentence.replace(" ", "").lower()

if check == check[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")