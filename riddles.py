from time import sleep
print("Приветствуем вас в игре: 'Отгадай загадку'.", flush = True)
sleep(2)
print("Всего - 3 загадки. За каждый правильный ответ дается 1 балл.", flush = True)
sleep(2)
print("Если вы наберете не меньше 2 баллов - выиграете, в противном случае - проигрыш", flush = True)
sleep(2)
print("Введите 'да', если готовы играть, 'нет' - не готовы", flush = True)
answer = input()
count = 0
if answer == "нет" or answer == "Нет" or answer == "НЕТ":
    print(":(", flush = True)
    sleep(4)
elif answer == "Да" or answer == "да" or answer == "ДА":
    from time import sleep
    print("Начнем!", flush=True)
    sleep(1.5)
    print("В Полотняной стране", flush=True)
    sleep(1.5)
    print("По реке Простыне", flush=True)
    sleep(1.5)
    print("Плывет пароход", flush=True)
    sleep(1.5)
    print("То назад, то вперед", flush=True)
    sleep(1.5)
    print("А за ним такая гладь —", flush=True)
    sleep(1.5)
    print("Ни морщинки не видать", flush=True)
    sleep(3)
    print("")
    print('Ваш ответ?')
    a = input()
    if a == "Утюг" or a == "утюг" or a == "УТЮГ":
        count += 1
        print("Ответ правильный! Вы набрали", count, "балл!", flush = True)
    else:
        print("Ответ неправильный. У вас", count, "баллов", flush = True)
    sleep(2)
    print("Продолжим!")
    sleep(1.5)
    print("Стоит дуб,", flush = True)
    sleep(1.5)
    print("В нем двенадцать гнезд,", flush = True)
    sleep(1.5)
    print("В каждом гнезде", flush = True)
    sleep(1.5)
    print("По четыре яйца,", flush = True)
    sleep(1.5)
    print("В каждом яйце", flush = True)
    sleep(1.5)
    print("По семи цыпленков.", flush = True)
    sleep(3)
    print("")
    print('Ваш ответ?')
    b = input()
    if b == "Год" or b == "год" or b == "ГОД":
        count += 1
        if count == 1:
            print("Ответ правильный! Вы набрали", count, "балл!")
        else:
            print("Ответ правильный! Поздравляем, вы выиграли!", flush = True)
            sleep(4)
            import sys
            sys.exit()
    else:
        if count == 1:
            print("Ответ неправильный.У вас", count, "балл")
        else:
            print('Ответ неправильный. Сожалеем, но вы проиграли.', flush = True)
            sleep(4)
            import sys
            sys.exit()
    print("Продолжим!")
    sleep(1.5)
    print("Ёжик странный у Егорки", flush = True)
    sleep(1.5)
    print("На окне сидит в ведерке.", flush = True)
    sleep(1.5)
    print("День и ночь он дремлет,", flush = True)
    sleep(1.5)
    print("Спрятав ножки в землю.", flush = True)
    sleep(3)
    print("")
    print('Ваш ответ?')
    c = input()
    if c == "Кактус" or c == "кактус" or c == "КАКТУС":
        print("Ответ правильный! Поздравляем, вы выиграли!", flush = True)
        sleep(4)
    else:
        print("Ответ неправильный. Сожалеем, вы проиграли.", flush = True)
        sleep(4)
        import sys
        sys.exit
else:
    print("Ошибка ввода", flush = True)
    sleep(4)
