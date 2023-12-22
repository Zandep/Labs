#  Вычислить сумму знакопеременного ряда |х(3n)|/(3n)!, где х-матрица ранга к (к и матрица задаются случайным образом),
# n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
# У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого  +.
import numpy as np
import random
from decimal import Decimal, getcontext

def custom_sum(x, t):
    n = 1
    z = 1
    curr_sum = 0
    curr_term = 0
    while abs(curr_term) < t:
        z *= 3*n * (3*n - 1) * (3*n - 2)
        curr_x = np.linalg.det(x * 3 * n)
        curr_term = Decimal(curr_x) / z
        curr_sum += curr_term * (-1) ** (n - 1)
        n += 1
    return curr_sum

try:
    t = int(input("Введите число t-количеством знаков после запятой: "))
    while t > 100 or t < 1:  # ошибка в случае введения слишком малой точности
        t = int(input("Вы ввели число, неподходящее по условию, введите число t, большее 1: \n"))
    print()
    k = random.randint(1, 10)
    x = np.random.randint(0, 10, (k, k))
    print("Сгенерированная матрица:")
    print(x)
    print()

    getcontext().prec = t + 100
    result = custom_sum(x, t)
    print(f"Сумма ряда с точностью {t} знаков после запятой: {result:.{t}f}")

except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")
