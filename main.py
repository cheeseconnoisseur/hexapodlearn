import random
import numpy as np
import os


lives = 200
dimensions = 5
mr = 30
starter = 0
c = ","
biglist = []

def main():
    start()
    print("lol")
    bigman()


##def start():
##    starter = 0
##    for i in range(lives):
##        #lol = np.zeros(5)
##        lol = [0,0,0,0,0]
##        bigint = random.randint(1,dimensions-1)
##        lol[bigint] = 1
##        print(lol)
###        np.savetxt('log.txt', lol)
##        if starter == 0:
##            starter = starter + 1
##            with open('log.txt', 'w') as f:
##                lol = str(lol)
##                f.write(lol)
##                f.write('\n')
##                f.close()
##        else:
##            with open('log.txt', 'a') as f:
##                lol = str(lol)
##                f.write(lol)
##                f.write('\n')
##                f.close()
def rnd(uganda):
    print(uganda)

    
def start():
    starter = 0
    for i in range(lives):
        #lol = np.zeros(5)
        lol = [0,0,0,0,0]
        bigint = random.randint(0,dimensions-1)
        lol[bigint] = 1
        print(lol)
        for i in range(5):
            lol[i-1] = str(lol[i-1])
        lol = lol[0] + c + lol[1] + c + lol[2] + c + lol[3] + c + lol[4]
        print(lol)
#        np.savetxt('log.txt', lol)
        if starter == 0:
            starter = starter + 1
            with open('log.txt', 'w') as f:
                f.write(lol)
                f.write(",,")
                f.close()
        else:
            with open('log.txt', 'a') as f:
                f.write(lol)
                f.write(",,")
                f.close()

def bigman():
    #lol = os.path.isfile('mydirectory/myfile.txt')
    #if lol == True:
    mkay = []
    with open('log.txt', 'r') as f:
            lol = f.read()
            print(lol)
            lol = lol.split(",,")
            lol = lol[:-1]
            f.close()
    print(lol)
    for i in range(lives-1):
        loltemp = lol[i-1].split(',')
        for i in range(dimensions):
            loltemp[i] = int(loltemp[i])
        biglist.append(loltemp)
        
    print(biglist)
        

main()
