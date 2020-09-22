import random
import csv
import re

class Hangman:

    def __init__(self,hangman):
        self.hangman = hangman
        self.myAnswer = []
        self.alphabets = []

    def csvToList(self):
        words = []
        with open('test.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                strRow = ''.join(map(str, row))
                regex = '[a-zA-Z]+'
                word = re.findall(regex, strRow)
                # word = str(word).strip("[\'").strip("\']") when you use append()
                words.extend(word)
        f.close()
        answer = str(random.choice(words))
        lenAnswer = len(answer)
        return answer, lenAnswer

    def wonLostPlayAgain (self,guess,answer):
        if set(answer) == set(self.myAnswer):
            print("You are the winner today!")
            self.hangman = 0
            return self.hangman
        elif self.hangman <= 0 :
            strAnswer = ''.join(map(str, answer))
            print("You just lost. The answer was ",str(strAnswer), ".")
            return self.hangman
        else:
            self.alphabets.append(guess)
            print("Try again.")
            return self.hangman

    def playS (self):
        answer, lenAnswer = self.csvToList()
        print("This is ", lenAnswer, " alphabet word. Good luck to guess.")
        while self.hangman > 0:
            guess = input("Please enter your alphabet: ")
            if guess.lower() in self.alphabets: print("You have already tried ",guess.upper()," alphabet!")
            elif len(guess) >= 2: print("You are allowed to put only 1 alphabet at once.")
            elif guess == str(0) or guess == str(1):
                print(answer, " is the answer. You lose!")
                # break
                print("my answer: ",set(self.myAnswer)," answer: ",set(answer))
            elif guess.isdigit(): print("You are allowed to put only alphabet, but no number.")
            elif guess.lower() in answer:
                print(guess, " was the right one!")
                self.myAnswer.append(guess)
            else: self.hangman -= 1

            self.hangman = self.wonLostPlayAgain (guess,answer)

    def playP(self):
        answer = input("Please enter your puzzle's answer. Then, the computer will guess some word. ")
        digit = len(answer)
        print("The computer will guess ", digit, " alphabet word.")
        computerAnswer = []
        self.alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        while self.hangman > 1:
            computerAnswerKey = ''.join(random.choice(self.alphabets) for i in range(1))
            self.alphabets.remove(computerAnswerKey)
            if computerAnswerKey.lower() in answer:
                print("This alphabet is correct: ", computerAnswerKey)
                computerAnswer.append(computerAnswerKey)
                if computerAnswer == answer.upper():
                    print("You just lost the game!")
                    break
            else:
                print("This alphabet is wrong: ", computerAnswerKey)
                self.hangman -= 1
                print("Try another alphabet.")
                if self.hangman == 0:
                    print("The answer was", answer, ". Congrats! You just won the game!")

    def playGame (self):
        yourRole = input("Would you want to be a solver or a puzzle giver? [s/p] ")
        if yourRole.lower() == 's' : self.playS()
        elif yourRole.lower() == 'p' : self.playP()
        else : print("You have to choose either s/p ")

if __name__ == '__main__':
    hangman1 = Hangman(6)
    print(hangman1.playGame())
