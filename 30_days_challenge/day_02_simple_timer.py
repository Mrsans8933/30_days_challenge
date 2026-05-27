import time
import winsound
try:
    timer = int(input("Введите через сколько таймеру сработать (В секундах): "))
except ValueError:
    print("Ошибка, похоже вы ввели НЕ число, перезапустите программу")
    exit()
for i in range(timer,0,-1):
    print(f"\r {i}c", end="")
    time.sleep(1)
print("\rТаймер сработал")
winsound.Beep(1000, 1000)
