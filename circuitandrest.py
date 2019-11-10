#! python3
# chrono per palestra! circuiti di crossfit

import time
from playsound import playsound

inizio=time.time()

while(True):
    try:
        print ("quanti secondi vuoi nel tuo circuito?")
        x=int(input())
        print ('quanto riposo?')
        y=int(input())
        break
    except:
        continue

print("START!!!!!!!!")

playsound('/home/thresorts/Dev/circuit/sound1.wav')

try:
    while(True):
        for i in range(0,x):
            print(x-i-1)
            time.sleep(1)
        playsound('/home/thresorts/Dev/circuit/sound1.wav')
        print('\n\tRIPOSO\n')
        for i in range (0,y):
            print('\t'+str(y-i-1))
            time.sleep(1)
        playsound('/home/thresorts/Dev/circuit/sound1.wav')
        print('\n\tLAVORO\n')
except:

    fine=time.time()

    print ("tempo totale")
    print ((fine-inizio)/60)
    print ("tempo di lavoro")
    lavoro=((fine-inizio)/60)*(x/(x+y))
    print (lavoro)

