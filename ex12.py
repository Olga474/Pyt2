print('Введите сумму чисел:', end=" ")
n = int(input())
if n <= 0:
    print('Некорректный ввод')
    raise SystemExit(1)
print('Введите произведение чисел:', end=" ")
m = int(input())
if m <= 0:
    print('Некорректный ввод')
    raise SystemExit(1)
for i in range(1000):
    for j in range(1000):
        if ((i + j + 2) == n) and ((i + 1) * (j + 1) == m):
            print('Петя загадал числа ' + str(i + 1) + ' и ' + str(j + 1))
            raise SystemExit(0)
