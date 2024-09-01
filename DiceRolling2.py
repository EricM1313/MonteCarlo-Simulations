import random

def trial():
    li = []
    for i in range(10):
        li.append(random.randint(1,6))
    print(li)
    return len(set(li))



def test(t):
    count = 0
    for i in range(t):
        count += trial()
    return count/t
    
    
#print(test(99999))

print(trial()) 