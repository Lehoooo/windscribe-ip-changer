## Made By Leho - github.com/lehoooo
import os
import time
import random
from datetime import datetime

timetowait = 5

currenttime = datetime.now()
regions = ["Sydney", "Melbourne", "Brisbane", "Canberra", "Perth"] # define locations here

print("windscribe auto ip changer - Made By Leho")
print("starting..")

while True:
    print("-----------------------------------------")
    print("rotating ip now")
    randregion = random.choice(regions)
    print(randregion)
    os.system("windscribe connect " + str(randregion))
    print("connected at " + str(currenttime))
    print("waiting " + str(timetowait) + " minutes")
    print("-----------------------------------------")
    time.sleep(int(timetowait) * 60)

    
