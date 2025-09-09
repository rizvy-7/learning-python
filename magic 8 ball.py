import random
num = random.randint(1, 100)
print(num)


question = input('Question:')
ran_ans = random.randint(1, 9)
if ran_ans == 1:
    print('Magic 8 Ball: Yes - Definitely')
elif ran_ans == 2:
    print('Magic 8 Ball: It is decidely so')
elif ran_ans == 3:
    print('Magic 8 Ball: Without a doubt')
elif ran_ans == 4:
    print('Magic 8 Ball: Reply hazy, try again')
elif ran_ans == 5:
    print('Magic 8 Ball: Ask again later')
elif ran_ans == 6:
    print('Magic 8 Ball: Better not tell you now')
elif ran_ans == 7:
    print('Magic 8 Ball: My sources say no')
elif ran_ans == 8:
    print('Magic 8 Ball: Outlook not so good')
else:
    print('Magic 8 Ball: Very doubtful')
