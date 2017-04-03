import subprocess
import time

# set these to whatever works for you
# sound will play when cpu load has been < IDLE_PERCENT for IDLE_TIME consecutive seconds
IDLE_TIME = 5
IDLE_PERCENT = 20

# you can execute any program you want by changing the alert function below


def get_load():
    output = subprocess.check_output('wmic cpu get loadpercentage', shell=True)
    load = output.split()[1]
    return int(load)

def alert():
    subprocess.call([
        r"c:\Program Files (x86)\Windows Media Player\wmplayer.exe",
        r"c:\Windows\Media\Windows Logon Sound.wav"])


idleSeconds = 0

while idleSeconds < IDLE_TIME:
    load = get_load()
    if load < IDLE_PERCENT:
        idleSeconds += 1
    else:
        idleSeconds = 0

    time.sleep(1)

alert()
