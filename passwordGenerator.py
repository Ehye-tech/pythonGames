import random
import shortuuid
import string

def passwordGenerator():
    print("Hello! This is password generator!")
    length = input("How long do you want your password? (Min :6, Max : 14) ")
    length = int(length)

    if length > 14 or length < 6:
        print("The minimum password must be length of 6 or more and the maximum must be less than and equal to 14.")
    else:
        alphanumeric = input("Do you want alphanumeric password? [y/n] ")
        if alphanumeric == 'y':
            specialSymbols = input("Do you want special symbols password? [y/n] ")
            if specialSymbols == 'y':
                ranSpecialAlphaNum(length)
            else:
                alphaNum(length)
        else:
            numOnly(length)

def alphaNum (length):
    yourPassword = shortuuid.ShortUUID().random(length=length)
    return print("This is your password : ", yourPassword)

def ranSpecialAlphaNum (length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    yourPassword = ''.join(random.choice(password_characters) for i in range(length))
    return print("This is your password : ", yourPassword)

def numOnly (length):
    yourPassword = ''.join(random.choice('0123456789') for i in range(length))
    return print("This is your password : ", yourPassword)

passwordGenerator()
