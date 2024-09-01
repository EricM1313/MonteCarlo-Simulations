import numpy as np

def trial():
    x=(np.random.poisson(300))
    y = (np.random.poisson(100))
    m = (2*x) + 5*y
    return m  
       

      


def trialS(t):
    tot = 0
    for i in range(t):
        tot+= trial()
    return  tot/t


print(trialS(100000))






