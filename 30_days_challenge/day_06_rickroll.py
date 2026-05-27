import webbrowser
import random
a = random.randint(1,2)
print("Выбери 1 или 2")
try:
    b = int(input())
    if a == b:
        print("Ок тебе фортануло")
    elif a != b:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        print("Введи число ОТ 1 до 2")
except ValueError:
    print("Ошибка введи число")
