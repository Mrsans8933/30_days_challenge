try:
    num = int(input("Введи число: "))
except:
    print("Ошибка, возможно вы ввели НЕ число.")
    exit()
try:
    choose = int(input(f"1.Найти факториал числа {num}\n2.Найти сумму арефметической прогрессии числа {num}\nТвой выбор:"))
except:
    print("Ошибка, возможно вы ввели НЕ число.")
    exit()
if choose == 1:
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print(fact)
elif choose == 2:
      prog = num * (num +1) //2
      print(prog)
else:
    print("Выбери либо 1 либо 2")
    