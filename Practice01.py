# learning if else elif function

import random
num = random.randint(0, 100)
print(num)
grade = 10

if grade >= 80:
    print("You have got A+")
elif grade >= 70:
    print("You have got A")
elif grade >= 60:
    print("You have got A-")
elif grade >= 50:
    print("You have got B")
elif grade >= 40:
    print("You have got C")
elif grade >= 33:
    print("You have got D")
else:
    print("You Failed!")
