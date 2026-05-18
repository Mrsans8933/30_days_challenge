import time
import keyboard
input("Нажмите Enter для запуска секундомера")
sec = 0
while True:
    print(f"\r{sec}", end="")
    time.sleep(1)
    sec += 1
    if keyboard.is_pressed("esc"):
        break

