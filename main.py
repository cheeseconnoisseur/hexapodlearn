import random
import numpy as np
import os

###have another .py file to get the txt file using the whole serial thing, this only mutates it ####
####https://www.arduino.cc/en/Tutorial/BuiltInExamples####
#####https://pyserial.readthedocs.io/en/latest/examples.html####
#####https://github.com/pyserial/pyserial####

#####for rasbery pi thing maybe?####
###https://www.raspberrypi.org/documentation/usage/python/####


lives = 200
dimensions = 5
mr = 30
starter = 0
c = ","
biglist = []

def main():
    #remove start if random set of input variables have already been created.
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
def rnd(uga):
    uganda = random.randint(0,uga)
    return uganda

    
def start():
    starter = 0
    for i in range(lives):
        #lol = np.zeros(5)
        lol = [0,0,0,0,0]
        bigint = rnd(dimensions-1)
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
    mutator(biglist)

def mutator(biglist):
    for i in range(lives):
        ranum = rnd(100)
        if ranum <= mr:
            lol = [0,0,0,0,0]
            bigint = rnd(dimensions-1)
            lol[bigint] = 1
            print(lol)
            #for j in range(5):
            #    lol[j-1] = str(lol[j-1])
            #lol = lol[0] + c + lol[1] + c + lol[2] + c + lol[3] + c + lol[4]
            #lol = str(lol[0]) + c + str(lol[1]) + c + str(lol[2]) + c + str(lol[3]) + c + str(lol[4])
            #biglist[i] = "gay"
            #print(lol)
            #lol = lol.split(",")
            #print(lol)
            biglist[i-1] = lol
        
            
    #print(biglist)
    writer(biglist[:-1])

def writer(biglist):
    os.remove("log.txt")
    for i in range(lives-1):
        man = biglist[i-1]
        for j in range(dimensions):
            man[j-1] = str(man[j-1])
        print(man)
        ",".join(man)
        man = str(man)
        
        with open('log.txt', 'a') as f:
            man = man.replace("[","")
            man = man.replace("]","")
            man = man.replace("'","")
            f.write(man)
            f.write(",,")
            f.close()
        
        
        

main()
