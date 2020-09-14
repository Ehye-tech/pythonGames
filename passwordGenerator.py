import random
import shortuuid

def passwordGenerator():

    print("Hello! This is password generator!")
    length = input("How long do you want your password? (Min :6, Max : 14) ")
    length = int(length)

    if length > 14 or length < 6:
        print("The minimum password must be length of 6 or more and the maximum must be less than and equal to 14.")
    else:
        alphanumeric = input("Do you want alphanumeric password? [y/n] ")
        alphaNum(alphanumeric,length)



def alphaNum(alphanumeric,length):

    if(alphanumeric.upper().lower() == 'y'):
        yourPassword = shortuuid.ShortUUID().random(length=length)
        return print("This is your password : ", yourPassword)
    else:
        yourPassword = ''.join(random.choice('0123456789') for i in range(16))
        return print("This is your password : ", yourPassword)

passwordGenerator()
