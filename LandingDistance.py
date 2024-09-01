import numpy as np


def land():
    xone = (np.random.normal(0,100))
    yone = (np.random.normal(0,100))
    xtwo = (np.random.normal(0,100))
    ytwo = (np.random.normal(0,100))
    return ((xone-xtwo)**2+(yone-ytwo)**2)**.5

def averagetrials(trials):
    tot = 0
    for t in range(trials):
        tot+= land()
    return tot/trials


print(averagetrials(10000))