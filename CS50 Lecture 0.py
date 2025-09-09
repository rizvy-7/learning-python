# parameters in print function
# sep and end
name = input("What's your name?")
print("Hello, ", name, sep="My dear ", end="")
print(". How are you?")

# how to use "" in a print function
print("He said, \"I am fine.\"")

# formatted string literals (f-strings)
age = 20
print(f"You are {age} years old.")
print(f"In 5 years, you will be {age + 5} years old.")

# escape sequences
print("First Line\nSecond Line")
print("Column1\tColumn2\tColumn3")
print("This is a backslash: \\")
print("She said, \"Hello!\"")

# string methods
name = name.strip()  # Remove leading/trailing whitespace`) name is from the first line
name = name.upper()  # Convert to uppercase
name = name.capitalize()  # Capitalize the first letter
name = name.title()  # Title case
print("Hello", name)

# string methods
# strip removes extra spaces and title makes first letter capitalized
title = input("Write down your full name: ").strip().title()

print("Hello", title)
