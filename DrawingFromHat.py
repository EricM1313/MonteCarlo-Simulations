import random 
import math

def gen():
    hat = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
    return hat[random.randint(0,29)]


def game():
    hand = []
    while (hand.count(0)+hand.count(1) < 8):
        hand.append(gen())
    return hand.count(2)


def trial(t):
    count = 0
    for i in range(t):
        count += game()
    return count/t

print(trial(10000))