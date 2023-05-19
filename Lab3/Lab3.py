# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
# заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# Формируется матрица F следующим образом: скопировать в нее А и если в Е количество нулевых элементов в нечетных столбцах в области 4 больше,
# чем количество отрицательных  элементов в четных строках в области 1,
# то поменять C и В симметрично области 4 и 3 местами, иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение:
# ((F+A)– (K * F) )*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.

import random
from copy import deepcopy

def print_matrix(mat):
    for row in mat:
        for elem in row:
          print('{:4}'.format(elem), end=' ')
        print()


def pastemat(matF, matrix, column_index, row_index):
    a = column_index
    for row in matrix:
      for element in row:
        matF[row_index][column_index] = element
        column_index += 1
      row_index += 1
      column_index = a


def matzero(size):
    return [[0 for i in range(size)] for j in range(size)]


def matrix_input(mat, i1, i2, j1, j2):
    zero_mat = matzero(len(mat)//2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zero_mat[i - i1][j - j1] = mat[i][j]
    return zero_mat


try:
    K = int(input('Введите число K: '))
    n = int(input('Введите число число N, больше или равное 5: '))
    while n < 5:
        n = int(input('Введите число N, большее или равное 5: '))
except ValueError:
    print('Введенный символ не является числом.')
    exit(0)

ans = input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: ')
if ans not in ['1', '2']:
    print('Попробуйте ещё')
    while ans not in ['1', '2']:
        n = int(input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: '))
if ans == '1':
    matA = [[(1) for i in range(n)] for j in range(n)]
elif ans == '2':
    matA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]


print('Матрица А изначальная:')
print_matrix(matA)

hn = n//2
fn = hn
if n % 2 != 0:
    fn += 1

matC = matrix_input(matA, 0, hn, fn, n)
matE = matrix_input(matA, fn, n, fn, n)
matD = matrix_input(matA, fn, n, 0, hn)
matB = matrix_input(matA, 0, hn, 0, hn)

print('Подматрицы матрицы A:')
print('Подматрица B')
print_matrix(matB)
print('Подматрица С')
print_matrix(matC)
print('Подматрица D')
print_matrix(matD)
print('Подматрица E')
print_matrix(matE)

zero, otr = 0, 0
for i in range(n // 4, hn):
    for j in range(hn - i - 1, i + 1):
        if j % 2 != 0 and matE[i][j] == 0:
            zero += 1
print('количество нулевых элементов в нечетных столбцах в области 4:', zero)

for i in range((n // 4) + 1):
    for j in range(i, hn - i):
        if j % 2 == 0 and matC[j][i] < 0:
            otr += 1
print('количество отрицательных  элементов в четных строках в области 1:', otr)

if zero > otr:
    print('количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество отрицательных  элементов в четных строках в области 1')
    print('Начальная подматрциа B:')
    print_matrix(matB)
    for i in range((n // 4) + 1):
        for j in range(i, hn - i):
            matB[i][j], matB[j][i] = matB[j][i], matB[i][j]
    print('Получившаяся подматрица B:')
    print_matrix(matB)
else:
    print('Количество нулевых элементов в нечетных столбцах в области 4 меньше или равно, чем количество отрицательных  элементов в четных строках в области 1')
    matE, matB = matB, matE

matF = deepcopy(matA)
pastemat(matF, matB, 0, 0)
pastemat(matF, matC, fn, 0)
pastemat(matF, matE, fn, fn)
pastemat(matF, matD, 0, fn)

print('Матрица F:')
print_matrix(matF)

matAt = matzero(n)
matFA = matzero(n)
matKF = matF.copy()

print('Вычисляем ((F+A) – (K * F))*AT:')

for i in range(n):
    for j in range(n):
        matFA[i][j] = matF[i][j] + matA[i][j]
print('Результат F + A:')
print_matrix(matFA)

for i in range(n):
    for j in range(n):
        matKF[i][j] *= K
print('Результат K * F:')
print_matrix(matKF)

matFAK = matzero(n)
for i in range(n):
    for j in range(n):
        matFAK[i][j] = matFA[i][j] - matKF[i][j]
print('Результат (F+A) – (K * F):')
print_matrix(matFAK)

print("Матрица A транспонированая:")
for i in range(n):
    for j in range(n):
        matAt[i][j] = matA[j][i]
print_matrix(matAt)

res = matzero(n)
for i in range(n):
    for j in range(n):
        res[i][j] = matFAK[i][j] + matAt[i][j]
print('Результат:')
print_matrix(res)
