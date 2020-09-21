import random
import csv
import re



hangman = 6

def csvToList ():
    words = []
    with open('test.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            strRow = ''.join(map(str, row))
            regex = '[a-zA-Z]+'
            word = re.findall(regex, strRow)
            word = str(word).strip("[\'").strip("\']")
            words.append(word)
    f.close()
    answer = str(random.choice(words))
    lenAnswer = len(answer)
    return words, answer, lenAnswer

def wonLostPlayAgain (hangman,alphabets,guess,answer,myAnswer):

    if set(answer) == set(myAnswer):
        print("You are the winner today!")
        hangman = 0
        return hangman
    elif hangman == 0 :
        strAnswer = ''.join(map(str, answer))
        print("You just lost. The answer was ",str(strAnswer), ".")
        return hangman
    else:
        if hangman > 0:
            alphabets.append(guess)
            print("Try again.")
            return hangman

def playS (hangman):

    hangman = hangman
    myAnswer = []
    alphabets = []
    words, answer, lenAnswer = csvToList ()
    
    print("This is ", lenAnswer, " alphabet word. Good luck to guess.")

    while hangman > 0 :
        guess = input("Please enter your alphabet: ")
        if guess.lower() in alphabets: print("You have already tried ",guess.upper()," alphabet!")
        elif len(guess) >= 2: print("You are allowed to put only 1 alphabet at once.")
        elif guess == str(0) or guess == str(1): 
            print(answer, " is the answer. You lose!")
            # break
            print("my answer: ",set(myAnswer)," answer: ",set(answer))
        elif guess.isdigit(): print("You are allowed to put only alphabet, but no number.")
        elif guess.lower() in answer:
            print(guess, " was the right one!")
            myAnswer.append(guess)
        else: hangman -= 1

        hangman = wonLostPlayAgain (hangman,alphabets,guess,answer,myAnswer)

def playP(hangman):
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

def playGame ():
    yourRole = input("Would you want to be a solver or a puzzle giver? [s/p] ")
    if yourRole.lower() == 's' : playS(hangman)
    elif yourRole.lower() == 'p' : playP(hangman)
    else : print("You have to choose either s/p ")


playGame()
