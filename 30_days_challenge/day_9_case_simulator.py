import random
drop = ["Обычный","Необычный","Эпический","Мифический","Легендарный"]
while True:
    input("Нажмите Enter для прокрута кейса")
    new_drop = random.randint(1,100)
    if new_drop <= 50:
        print(drop[0])
    elif new_drop > 50 and new_drop <= 80:
        print(drop[1])
    elif new_drop > 80 and new_drop <= 95:
        print(drop[2])
    elif new_drop > 95 and new_drop <= 99:
        print(drop[3])
    elif new_drop == 100:
        print(drop[4])
