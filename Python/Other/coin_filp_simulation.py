from random import randint
import time 

heads_47 = 0
tails_47 = 0
rolls = int(input("How many rolls: "))

now = time.time()

for y in range(rolls):
    heads = 0
    tails = 0

    for x in range(100):

        roll = randint(0, 1)

        if roll == 1:
            heads += 1
        else: 
            tails += 1

    print (f"Heads: {heads} Tails: {tails}")

    if heads == 47:
        heads_47 += 1
    
    if tails == 47:
        tails_47 += 1

print (f"Number of times heads == 47: {heads_47}")
print (f"Number of times tails == 47: {tails_47}")
elasped_time = time.time() - now
print (f"Elapsed time {elasped_time:.4f} ms")