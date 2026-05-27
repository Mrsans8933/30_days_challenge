print("Конвертер валют")
euro_price = 83
dollar_price = 71

try:
    choose = int(input("1.Рубль в...\n2...в рубль\nВыбор:"))
except ValueError:
    print("Ошибка, веедите число")
    exit()
if choose == 1:
    try:
        choose = int(input("1.Рубль в доллар\n2.Рубль в евро\nВыбор:"))
    except ValueError:
        print("Ошибка, веедите число")
        exit()

    if choose == 1:
        try:
            rub = float(input("Сколько рублей в доллар конвертировать: "))
        except ValueError:
            print("Ошибка, веедите число")
            exit()
        print(f"{rub} Рублей = {rub/dollar_price:.2f} доллара")
        exit()

    elif choose == 2:
        try:
            rub = float(input("Сколько рублей в евро конвертировать: "))
        except ValueError:
            print("Ошибка, веедите число")
            exit()
        print(f"{rub} Рублей = {rub / euro_price:.2f} евро")
        exit()

    else:
        print("Ошибка, возможно вы ввели не верное значение")

elif choose == 2:
    try:
        choose = int(input("1.Доллар в рубль\n2.Евро в рубль\nВыбор:"))
    except ValueError:
        print("Ошибка, веедите число")
        exit()
    if choose == 1:
        try:
            input_dollar = float(input("Сколько долларов в рубли конвертировать: "))
        except ValueError:
            print("Ошибка, веедите число")
            exit()
        print(f"{input_dollar} долларов в рубли будет: {input_dollar * dollar_price:.2f} рублей")
        exit()
    elif choose == 2:
        try:
            input_euro = float(input("Сколько евро в рубли конвертировать: "))
        except ValueError:
            print("Ошибка, веедите число")
            exit()
        print(f"{input_euro} евро в рубли будет: {input_euro * euro_price:.2f} рублей")
        exit()
    else:
        print("Ошибка, возможно вы ввели не верное значение")
else:
        print("Ошибка, возможно вы ввели не верное значение")
