print("Оценка сложности пароля")
password = input("Введи ваш пароль для оценки: ")
length = len(password)
more_8 = False
letter = False
letters = "qwertyuioasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"

for i in password:
    if i in letters:
        letter = True
if length > 8:
    more_8 = True
else:
    print("Пароль короткий")
if more_8 == False:
    print("Пароль СЛИШКОМ слабый")
elif more_8 == True and letter == False:
    print("Пароль слабый, добавьте букву")
elif more_8 == True and letter == True:
    print("Пароль надежен")