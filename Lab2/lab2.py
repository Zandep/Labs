import re

number_to_words = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'ноль'}
number_counter = 0

try:
    file = open("text.txt", "r")  # открываем файл
    while True:
        a = file.readline().split()  # читаем строку
        #        print(a)
        if not a:  # если файл пустой
            print("\nФайл text.txt в директории проекта закончился.")
            break
        for j in a:
            res = re.findall(r'(?<![\w/\;!?\\])\d+(?=[.,!?;])?(?!\w)', j)  # находим все натуральные числа с учетом грамматики
            counter = 0  # счетчик для вывода
            number_counter += 1
            if len(res) == 2 and int(res[0]) != 0:
                for i in str(int(res[0])):  # вывод
                    print(i,end="")
                for g in str(int(res[1])):
                    print(number_to_words[int(g)],end="")
                print()

    if number_counter == 0:  # если чисел, подходящих условию нет
        print()
        print('В файле нет чисел, удовлетворяющих условию. Добавьте числа в файл или переименуйте существующий *.txt файл.')

except FileNotFoundError:
    print()
    print("\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
