import random as rand

def rollDice():
    return (rand.randint(1,6))

def roll3Dice():
    A = rollDice()
    B = rollDice()
    C = rollDice()
    l = [A,B,C]
    if (l.count(4) == 2 or l.count(2)==1 or l.count(6)==1):
        return True
    return False

def simulate(number):
    hit = 0
    tot = 0
    for i in range(number):
        if (roll3Dice()):
            hit +=1
            tot+=1
        else:
            tot += 1
    return(hit/tot)

print(simulate(100000))