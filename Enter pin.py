# Learning Loop(While)
print("BANK OF CODEDEX")

pin = int(input("Enter your pin: "))

while pin != 1234:
    pin = int(input("Incorrect pin, Enter your pin again: "))

if pin == 1234:
    print("PIN Accepted!")

# guess the number

guess = int(input("Guess a number between 1-10:  "))

while guess != 7:
    guess = int(input("You are incorrect, Guess again"))

print("Congratulations!!")
