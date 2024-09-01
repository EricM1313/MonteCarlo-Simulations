import random as rand

items_to_collect = 10
trials = 100


def collect(items_to_collect):
    count = 0
    collection = []
    while (len(set(collection)) < items_to_collect):
        collection.append(rand.randint(1,items_to_collect))
        count +=1
    return count



def multipleTrials(trials,items_to_collect):
    total = 0
    for t in range(trials):
        total += collect(items_to_collect)
    return total/trials



print(multipleTrials(trials,items_to_collect))