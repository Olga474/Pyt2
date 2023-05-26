print('Введите количесвто монеток:', end=" ")
n = int(input())

r = 0
o = 0
print('Введите сторону монетки (0 если решка, 1 если орел):')
for i in range(n):
    print(str(i+1) + ' монетка: ', end=" ")
    m = int(input())
    if (m == 0):
        r += 1
    elif (m == 1):
        o += 1
    else:
        print('Некорректное значение')
        raise SystemExit(1)

if r > o:
    print ('Нужно перевернуть ' + str(o) + ' монет')
else:
    print ('Нужно перевернуть '+ str(r) + ' монет')