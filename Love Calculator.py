import random

name1 = str(input("Enter your name: "))
name2 = str(input("Enter your crush or partner name: "))

per1 = range(90,101)
per2 = range(83,101)
per3 = range(77,101)
per4 = range(7,86)

if name1[0] == name2[0] and len(name1) == len(name2):
    love1 = random.choice(per1)
    print("Your love percentage is",love1) 
elif name1[0] == name2[0]:
    love2 = random.choice(per2)
    print("Your Love percentage is",love2)

elif len(name1) == len(name2):
    love3 = random.choice(per3)
    print("Your Love percentage is",love3)
else:
    love4 = random.choice(per4)
    print("Your Love percentage is",love4)
