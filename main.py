import random
import numpy as np


lives = 200
dimensions = 5
mr = 30

def main():
    start()


def start():
    for i in range(lives):
        lol = np.zeros(5)
        bigint = random.randint(1,dimensions-1)
        lol[bigint] = 1
        print(lol)
        with open('log.txt', 'a') as f:
            lol = str(lol)
            f.write(lol)
            f.write('\n')
            f.close()

main()
