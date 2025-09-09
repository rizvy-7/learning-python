# This program adds two integers provided by the user
x = int(input("Enter a number:"))
y = int(input("Enter another number:"))

print(x + y)


# This program adds two floating-point numbers provided by the user
a = float(input("Enter a number:"))
b = float(input("Enter another number:"))

z = round(a + b)

print(f"{z:,}")

# round
c = float(input("Enter a number:"))
d = float(input("Enter another number:"))
z = round(c / d, 2)

print(z)

# round 2

e = float(input("Enter a number:"))
f = float(input("Enter another number:"))
z = (e / f)
print(f"{z:.2f}")  # 2 decimal places
