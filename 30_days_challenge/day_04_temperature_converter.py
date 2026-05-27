choose = int(input("1.°C в °F\n2.°F в °C\nВаш выбор:"))
if choose == 1:
    C = float(input("Введите сколько перевести"))
    print(f"{C*9/5+32}°F")
elif choose == 2:
    F = float(input("Введите сколько перевести"))
    print(f"{(F-32)*5/9}°C")
