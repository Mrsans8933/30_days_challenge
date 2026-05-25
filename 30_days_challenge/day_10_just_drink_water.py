import winsound as ws
import time

cooldown = 1800
while True:
    time.sleep(cooldown)
    ws.Beep(1000, 1000)
    ws.Beep(1000, 1000)
    ws.Beep(1000, 1000)
    print("Выпей воды")
