import random
import csv
import re

hangman = 5

yourRole = input("Would you want to be a solver or a puzzle giver? [s/p] ")
if yourRole.lower() == 's':

    words = []
    with open('test.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            strRow = ''.join(map(str, row))
            regex = '[a-zA-Z]+'
            word = re.findall(regex, strRow)
            words.append(word)
    f.close()

    answer = str(random.choice(words))
    alphabets = []
    myAnswer = []
    length = len(answer)-4
    print("This is ", length, " alphabet word. Good luck to guess.")

    while hangman > 0:

        if set(answer) == set(myAnswer):
            print("You are the winner today!")
            break

        guess = input("Please enter your alphabet: ")

        if guess.lower() in alphabets:
            print("You have already tried ",guess.upper()," alphabet!")
        elif len(guess) >= 2:
            print("You are allowed to put only 1 alphabet at once.")
        elif guess.isdigit():
            print("You are allowed to put only alphabet, but no number.")
        else:
            if guess.lower() in answer:
                print(guess, " was the right one!")
                myAnswer.append(guess)

            # # check the answer for test the code
            # elif guess == str(0) or guess == str(1):
            #     print(answer, " is the answer. You lose!")
            #     # break
            #     print("my answer: ",set(myAnswer)," answer: ",set(answer))

            else:
                hangman -= 1
                if hangman > 0: print("Try again.")


        alphabets.append(guess)
        strAnswer = ''.join(map(str, answer))

    if hangman == 0 : print("You just lost. The answer was ",str(strAnswer), ".")

elif yourRole.lower() == 'p':

    answer = input("Please enter your puzzle's answer. Then, the computer will guess some word. ")
    digit = len(answer)
    print("The computer will guess ", digit, " alphabet word.")
    computerAnswer = []

    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

    while hangman > 0:

        computerAnswerKey = ''.join(random.choice(alphabets) for i in range(1))
        alphabets.remove(computerAnswerKey)

        if computerAnswerKey.lower() in answer:
            print("This alphabet is correct: ", computerAnswerKey)
            computerAnswer.append(computerAnswerKey)
            if computerAnswer == answer.upper():
                print("You just lost the game!")
                break

        else:
            print("This alphabet is wrong: ", computerAnswerKey)
            hangman -= 1
            print("Try another alphabet.")

            if hangman == 0:
                print("The answer was", answer, ". Congrats! You just won the game!")

else:
    print("You have to choose either s/p ")


