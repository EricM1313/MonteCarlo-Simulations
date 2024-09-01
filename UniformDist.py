import numpy as np
import random
import math

def trial():
    y = random.uniform(2,5)
    return 100/y

def many(n):
    count = 0
    for i in range(n):
        count += trial()
    return count/n


print(many(200000))