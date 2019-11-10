#! python3
# Pomodoro app to productivity

import subprocess
import time
import gi
from playsound import playsound

print("""
           ,d                                               ,d
           88                                               88
           MM88MMM ,adPPYba,  88,dPYba,,adPYba,  ,adPPYYba, MM88MMM ,adPPYba,
           88   a8"     "8a 88P'   "88"    "8a ""     `Y8   88   a8"     "8a
           88   8b       d8 88      88      88 ,adPPPPP88   88   8b       d8
           88,  "8a,   ,a8" 88      88      88 88,    ,88   88,  "8a,   ,a8"
           "Y888 `"YbbdP"'  88      88      88 `"8bbdP"Y8   "Y888 `"YbbdP"'

                                                            timer, by Ronin

                               _________________________

           """)

x = 25
start = time.time()
while(True):
    try:
        print("minutes? (default 25)")
        y = int(input())
        if (y != 0):
            x = y
        break
    except (EOFError, TypeError, ValueError):
        break
try:
    x *= 60
    # while(True):
    for i in range(0, x):
        print('\r', x-i, end='')
        time.sleep(1)
    # playsound('/home/ronin/Developer/apps/pomodoro/Beep-tone.mp3')
    subprocess.run(["mousepad", "z.txt"])

except(KeyboardInterrupt, SystemExit):
    print("manual interruption")

print("manual interruption (5 minutes recomended)")
