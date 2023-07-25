# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

a = abs(int(input('Введите число N ')))
stop = 0
P = 2
for i in range(a):
    if stop != 1:
        P = P ** i
        if P <= a:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = a