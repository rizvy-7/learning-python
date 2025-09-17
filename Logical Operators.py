hunger = int(input("Enter your hunger level: "))
cold = int(input("Enter your cold level: "))
if hunger < 10 or cold > 100:
    print('You Died!')
else:
    print('You are healthy')
