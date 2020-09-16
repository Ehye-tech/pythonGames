import random
import sys

yn = input("Let's start guessing number game! [y/n] ")

if 'y' == yn.lower():
    condition = True
    start = int(sys.argv[1])
    end = int(sys.argv[2])

else:
    condition = False
    print("No? The game will be terminated.")

rightNum = random.randrange(start,end,1)
print(start," - ",end, " is your range to guess.")

while(condition):

    yourNum = input("Enter your guess number : ")
    yourNum =int(yourNum)

    if(yourNum == rightNum):
        print("Excellent! The game will be terminated.")
        break

    else:
        if rightNum > yourNum: print(yourNum, " is smaller than the right number. Guess another number.")
        elif rightNum < yourNum: print(yourNum, " is bigger than the right number. Guess another number.")

        if yourNum == 0:
            print(rightNum, "was the answer! The game is done.")
            break

