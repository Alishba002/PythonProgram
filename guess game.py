import random
num = random.randint(0,100)
tries=0
while True:
    x = input("Enter the number :")
    tries = tries+1
    if x==num:
        print("you won the game")
        break;
    elif num < x:
        print("Your number is too small")
    elif num > x:
        print("your number is too high")
if tries>7:
    print("poor")
elif 6 < tries > 4:
    print("good")
elif tries < 3:
    print("Excellent")
