print('Введите N:')
n = int(input())
if n <= 0:
    print('Некорректный ввод')
    raise SystemExit(1)
k = 1
while (k <= n):
    print(k, end=" ")
    k = k*2
