import random

game = 1


def random_rps():
    rps = ["rock", "paper", "scissors"]
    randomRPS = random.choice(rps)
    return randomRPS


def play_again(wl: str):
    print("You just", wl)

    yn = input("Would you try again? [y/n] ")
    if yn.lower() == "n":
        global game
        game = 0
        return print("Game is done!")
    elif yn.lower() == "y":
        return print("Are you ready?")


def play_rps():
    while game == 1:
        rr = random_rps()
        yourRPS = input("Rock Paper Scissors shoot! ")
        print("You:", yourRPS, "!!")
        print("Computer:", rr, "!!")
        if yourRPS.lower() == rr:
            print("You just tie the game!")

        else:
            # if the player's winner
            if (yourRPS.lower() == "scissors" and rr == "paper") or (
                    yourRPS.lower() == "rock" and rr == "scissors") or (
                    yourRPS.lower() == "paper" and rr == "rock"):
                play_again("won")
            elif (yourRPS.lower() == "paper" and rr == "scissors") or (
                    yourRPS.lower() == "scissors" and rr == "rock") or (
                    yourRPS.lower() == "rock" and rr == "paper"):
                play_again("lost")



play_rps()


