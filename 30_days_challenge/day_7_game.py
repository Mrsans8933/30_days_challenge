import random
print("Игра камень,ножницы, бумага")
things = ["камень","ножницы","бумага"]
while True:
    random_thing = random.choice(things)
    player = input("Ваш выбор: ")
    player = player.lower()
    if player not in things:
        print("Ошибка введите только: Камень, ножницы или бумага ")
        continue
    print(f"ПК выбрал {random_thing}")
    if player == random_thing:
        print("Ничья")
    elif player == "камень" and random_thing == "ножницы" or\
        player == "бумага" and random_thing =="камень" or\
        player == "ножницы" and random_thing == "бумага":
        print("Вы победили")
    else:
        print("Вы проиграли")