barcode = [46073, 45411, 46024, 52324, 51424] # штрих коды соответствующих товаров (каждый столбец - код, цена, товар)
cost = ['32', '113', '84', '284', '56']
name = ['хлеб  ', 'яйца ', 'чай   ', 'курица', 'яблоки']
total = []
c = []
count = []
numb = []
print('Отсканируйте штрих-код товара:')
print('Когда все товары будут просканированы, введите - Итого.')
h = 'скан'
while h != 'Итого':
    h = input()
    for i in range(len(barcode)):
        barcode[i] = str(barcode[i])
        if h == barcode[i]:
            if barcode[i].startswith('5'):
                print(name[i])
                c.append(name[i])
                print('Укажите вес в г:')
                n = int(input()) 
                p = cost[i]
                count.append(p)
                p = int(p)
                print(name[i], '-', p*n/1000, 'rub')
                p = p*n/1000
                n = n / 1000
                n = str(n)
                numb.append(n)
                total.append(p)
                print('Отсканируйте следующий товар')
            else:
                print(name[i], '-', cost[i], 'руб')
                c.append(name[i])
                print('Укажите количество:')
                n = int(input())
                p = cost[i]
                count.append(p)
                p = int(p) * n
                total.append(p)
                n = str(n)
                numb.append(n)
                print('Отсканируйте следующий товар')
    if len(h) != 5:
        i = len(barcode)
        print('Неверный штрих-код')
if not total:
    print('Не скромничайте с покупками')
else:
    print('Отсканируйте скидочную карту магазина') # 1
    n = int(input())
    print('Название товара', '     ', 'цена', '       ', '  количество', '   Стоимость')
    for i in range(len(c)):
        t = total[i]
        t = int(t)
        print(c[i], '             ', count[i], 'руб', '           ', numb[i], '       ', t, 'руб')
    if n == 1:
        s1 = sum(total)
        s1 = int(s1)
        s2 = sum(total) * 0.95
        s2 = int(s2)
        print('                                    Итого к оплате без скидки:', s1, 'руб')
        print('                                    Итого к оплате со скидкой:', s2, 'руб')
        print('                                                       Скидка:', s1-s2, 'руб')
    else:
        s = sum(total)
        s = int(s)
        print('                                    Итого к оплате:', s, 'руб') 


