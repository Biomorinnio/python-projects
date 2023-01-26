print('Введите выражение, содержащее знак "=" в конце:') # например, (5 + 4 / 2 =)
print('Целую часть и дробную в десятичной дроби отделяйте точкой("1.5")')
s = input()
s = s.replace(' ', '')
l = []
f = []
flag = False
if s[-1] != '=':
    print('Нет знака равно ')
else:
    for i in range(len(s)):
        if s[i] != '*' and s[i] != '/' and s[i] != '+' and s[i] != '-' and s[i] != '=':
            l.append(s[i])
        else:
            a = ''.join(l)
            l = []
            f.append(a)
            if s[i] != '=':
                f.append(s[i])
    if '-' in f:
        a = int(f.index('-'))
        b = float(f[a+1])
        f.insert(a+1, -b)
        del f[a+2]

    if '/' in f and '*' in f:
        zx = int(f.index('*'))
        zd = int(f.index('/'))
        if zx < zd:
            if '*' in f:
                zx = int(f.index('*'))
                a = float(f[zx - 1])
                b = float(f[zx + 1])
                ax = float(a * b)
                f.insert(zx, ax)
                del f[zx-1]
                del f[zx]
                del f[zx]
            if '/' in f:
                zd = int(f.index('/'))
                a = float(f[zd-1])
                b = float(f[zd+1])
                if b == 0:
                    print('Ошибка, на ноль делить нельзя')
                    flag = True
                else:
                    ad = float(a / b)
                    f.insert(zd, ad)
                    del f[zd-1]
                    del f[zd]
                    del f[zd]
            if '+' in f:
                zp = int(f.index('+'))
                a = float(f[zp - 1])
                b = float(f[zp + 1])
                ad = float(a + b)
                f.insert(zp, ad)
                del f[zp - 1]
                del f[zp]
                del f[zp]
            if '-' in f:
                zm = int(f.index('-'))
                a = float(f[zm - 1])
                b = float(f[zm + 1])
                ad = float(a + b)
                f.insert(zm, ad)
                del f[zm - 1]
                del f[zm]
                del f[zm]
        else:
            if '/' in f:
                zd = int(f.index('/'))
                a = int(f[zd - 1])
                b = int(f[zd + 1])
                if b == 0:
                    print('Ошибка, на ноль делить нельзя')
                    flag = True
                    import sys
                    sys.exit()
                else:
                    ad = float(a / b)
                    f.insert(zd, ad)
                    del f[zd - 1]
                    del f[zd]
                    del f[zd]
            if '*' in f:
                zx = int(f.index('*'))
                a = float(f[zx - 1])
                b = float(f[zx + 1])
                ax = float(a * b)
                f.insert(zx, ax)
                del f[zx-1]
                del f[zx]
                del f[zx]
            if '+' in f:
                zp = int(f.index('+'))
                a = float(f[zp - 1])
                b = float(f[zp + 1])
                ad = float(a + b)
                f.insert(zp, ad)
                del f[zp - 1]
                del f[zp]
                del f[zp]
            if '-' in f:
                zm = int(f.index('-'))
                a = float(f[zm - 1])
                b = float(f[zm + 1])
                ad = float(a + b)
                f.insert(zm, ad)
                del f[zm - 1]
                del f[zm]
                del f[zm]
    if '*' in f and '/' not in f:
        zx = int(f.index('*'))
        a = float(f[zx - 1])
        b = float(f[zx + 1])
        ax = float(a * b)
        f.insert(zx, ax)
        del f[zx - 1]
        del f[zx]
        del f[zx]

        if '+' in f:
            zp = int(f.index('+'))
            a = float(f[zp - 1])
            b = float(f[zp + 1])
            ad = float(a + b)
            f.insert(zp, ad)
            del f[zp - 1]
            del f[zp]
            del f[zp]
        if '-' in f:
            zm = int(f.index('-'))
            a = float(f[zm - 1])
            b = float(f[zm + 1])
            ad = float(a + b)
            f.insert(zm, ad)
            del f[zm - 1]
            del f[zm]
            del f[zm]
    if '*' not in f and '/' in f:
        zd = int(f.index('/'))
        a = float(f[zd - 1])
        b = float(f[zd + 1])
        if b == 0:
            print('Ошибка, на ноль делить нельзя')
            flag = True
        else:
            ad = float(a / b)
            f.insert(zd, ad)
            del f[zd - 1]
            del f[zd]
            del f[zd]
        if '+' in f:
            zp = int(f.index('+'))
            a = float(f[zp - 1])
            b = float(f[zp + 1])
            ad = float(a + b)
            f.insert(zp, ad)
            del f[zp - 1]
            del f[zp]
            del f[zp]
        if '-' in f:
            zm = int(f.index('-'))
            a = float(f[zm - 1])
            b = float(f[zm + 1])
            ad = float(a + b)
            f.insert(zm, ad)
            del f[zm - 1]
            del f[zm]
            del f[zm]
    if '*' not in f and '/' not in f:
        if '+' in f:
            zp = int(f.index('+'))
            a = float(f[zp - 1])
            b = float(f[zp + 1])
            ad = float(a + b)
            f.insert(zp, ad)
            del f[zp - 1]
            del f[zp]
            del f[zp]
        if '-' in f:
            zm = int(f.index('-'))
            a = float(f[zm - 1])
            b = float(f[zm + 1])
            ad = float(a + b)
            f.insert(zm, ad)
            del f[zm - 1]
            del f[zm]
            del f[zm]
    if flag == False:
        answer = f[0]
        if float(answer) == int(answer):
            print(int(answer))
        else:
            print(round(answer, 3))


