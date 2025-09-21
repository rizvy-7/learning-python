guess = int(input("Guess the number: "))
tries = 0

while guess != 6 and tries < 5:
    guess = int(input('Guess the number: '))
    tries += 1
if guess != 6:
    print("You ran out of time")
else:
    print("Congrats!")
    print(f"You guessed the number in {tries + 1} tries.")
