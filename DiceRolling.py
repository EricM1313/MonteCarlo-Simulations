import random as rand

def diceExperiment():
    rolls=[]
    count = 0
    while (rolls.count(5) + rolls.count(6) < 10):
        count +=1
        rolls.append(rand.randint(1,6))
    return [count, rolls.count(2)]



def trial(trials):
    totalrolls = 0
    totaltwos = 0
    for t in range(trials):
        totalrolls += diceExperiment()[0]
        totaltwos += diceExperiment()[1]
    return [totalrolls/trials,totaltwos/trials]




print(trial(10000))
