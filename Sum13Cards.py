import random
import math


def exp():
    total = 0
    deck = []
    for i in range(1,14):
        for p in range(4):
            deck.append(i)
    for i in range(13):
        num = random.randint(0,len(deck)-1)
        total+= deck.pop(num)
    return total

def trialAv(t):
    tot = 0
    for i in range(t):
        tot+= exp()
    return tot/t


print(trialAv(10000))
