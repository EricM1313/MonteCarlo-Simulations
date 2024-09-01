import random as rand
import math


def game(p):
    if (rand.random() < p):
        return True
    return False


def series(p):
    TeamOne = 0
    TeamTwo = 0
    games = 0
    while (abs(TeamOne-TeamTwo)<2):
        if game(p):
            TeamOne +=1
        else:
            TeamTwo +=1
        games +=1
    return games




def trial(trials):
    runningTotal=0
    for t in range(trials):
        runningTotal += series(.6)
    return runningTotal/trials


print(trial(100000))