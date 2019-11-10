#! python3
# Pomodoro app to productivity

import time
import gi
from playsound import playsound

x = 25
start = time.time()
while(True):
    try:
        print("minutes? (default 25)")
        y = int(input())
        if (y != 0):
            x = y
        break
    except (EOFError, TypeError):
        continue
try:
    # x *= 60
    # while(True):
    for i in range(0, x):
        print(x-i)
        time.sleep(1)
    playsound('home/ronin/Developer/apps/pomodoro/Beep-tone.mp3')
except(KeyboardInterrupt, SystemExit):
    print("manual interruption")

print("manual interruption (5 minutes recomended)")
