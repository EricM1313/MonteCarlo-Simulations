import numpy as np




def trial():
    x = np.random.normal(0,1)
    z = np.random.normal(0,1)
    return (4*x  + 1)  < (-2.57*z)


c = 0
for i in range(100000):
    if trial():
        c += 1

print(c/100000)


    