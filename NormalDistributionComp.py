import numpy as np





def trial():
    count = 0
    x = np.random.uniform(0,1)
    for i in range(10):
        c = np.random.uniform(0,1)
        if (c<x):
            count += 1
        else:
            count += -1
    return count, x


l = []
tot = 0
c= 0
for i in range(10000):
    l.append(trial())

for e in l:
    
    if e[0] == 2:
        tot+= e[1]
        c += 1

print(trial())



    




