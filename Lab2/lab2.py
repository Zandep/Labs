import re

number_to_words = {'+':'+','-':'-',',':',','.':'.','1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль'}
number_counter = 0
koll = 0

try:
    file = open("text.txt", "r")
    while True:
        a = file.readline().split()
        if not a:
            print("\nФайл text.txt в директории проекта закончился.")
            break
        for j in a:
            res = re.findall(r'[-+]?(?<![\w/\;!?\\])\d*[.,]\d*', j)
            #print(''.join(res))
            number_counter += 1
            if len(res) == 1 and ''.join(res[0]) != 0:
                for i in ''.join(res[0]):
                    if i == '.' or i == ',':
                        koll += 1
                    if koll == 0:
                        print(number_to_words[str(i)], end=" ")
                    else:
                        print(i, end=" ")
                print()
                koll = 0

    if number_counter == 0:
        print()
        print('В файле нет чисел, удовлетворяющих условию. Добавьте числа в файл или переименуйте существующий *.txt файл.')

except FileNotFoundError:
    print()
    print("\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
