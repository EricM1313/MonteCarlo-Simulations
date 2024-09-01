import random

def fcard():
    lis = []
    for i in range(4):
        lis.append(random.randint(1,52))
    return lis

def good(l):
    s = 0
    h = 0
    for p in l:
        if (p<=13):
            s+= 1
        if (p<=26 and p>13):
            h+=1
    if s>=2 or h>=2:
        return True
    return False




def trial(n):
    suc = 0
    for i in range(n):
        if good(fcard()):
            suc += 1
    return suc/n


print(trial(100000))