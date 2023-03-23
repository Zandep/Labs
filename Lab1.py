slovar = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'ноль'}
numbers = {str(x) for x in range(10)}
symbols = {'.', ',', ' ', '"', "'"}

max_buffer_len = 100
buffer_len = 1

work_buffer = ""  # рабочий буфер
number_flag = False  # флаг числа
trash_flag = False  # флаг мусора между числами
work_buffer_len = buffer_len  # длина рабочего буфера

try:
    with open("text.txt", "r") as file:  # открываем файл
        print("\n------Результат работы программы-----\n")
        buffer = file.read(buffer_len)  # читаем первый блок
        if not buffer:  # если файл пустой
            print("\nФайл test.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:  # пока файл не пустой
            if buffer >= '0' and buffer <= '9':  # обрабатываем текущий блок
                number_flag = True
                work_buffer += slovar[int(buffer)]

            else:
                work_buffer += buffer
                if buffer >= '0' and buffer <= '9':
                    number_flag = True
                elif (buffer not in numbers) and (buffer not in symbols):  # проверка буфера на мусорные элементы
                    trash_flag = True

            if buffer.find(' ') >= 0 or buffer.find('"') >= 0 or buffer.find("'") >= 0:  # если символ, разделяющий числа
                if number_flag and not (trash_flag):  # если число
                    work_buffer = work_buffer[:-1]  # срезаем знак
                    print(work_buffer)  # печатаем число и готовим новый цикл
                    number_flag = False
                trash_flag = False
                work_buffer = ""
                work_buffer_len = 0
            buffer = file.read(buffer_len)  # читаем очередной блок
            work_buffer_len += buffer_len
            if work_buffer_len >= max_buffer_len and buffer.find('!') < 0 and buffer.find('?') < 0 and buffer.find('"') < 0 and buffer.find("'") < 0:
                print("\nФайл test.txt не содержит знаков, разделяющих числа, и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории проекта или переименуйте существующий *.txt файл.")
                buffer = ""

except FileNotFoundError:
    print("\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
