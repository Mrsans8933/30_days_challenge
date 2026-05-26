try:
    choose = int(input("1.См в дюймы\n2.Дюймы в см\nВаш выбор: "))
    if choose == 1:
        centimetres = float(input("Сколько см в дюймы вы хотите перевести: "))
        print(f"{centimetres} Сантиметров = {centimetres/2.54} дюймов")
    elif choose == 2:
        inches = float(input("Сколько дюймов в см вы хотите перевести: "))
        print(f"{inches} в см = {inches/0.39370078740157}")
except ValueError:
    print("Ошибка, возможно вы ввели не число")