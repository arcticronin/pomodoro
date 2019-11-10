#! python3
# chrono per palestra! circuiti di crossfit

import time
import gi
from playsound import playsound

start=time.time()
while(True):
    try:
        print ("quanti secondi vuoi nel tuo circuito?")
        x=int(input())
        break
    except:
        continue
try:
    while(True):
        for i in range(0,x):
            print(x-i)
            time.sleep(1)
        playsound('/home/thresorts/Dev/circuit/sound1.wav')
except:
    tot=(time.time()-start)
    print("FINE ALLENAMENTO, è durato:")
    print(round(tot/60 , 2))
    print("minuti")

