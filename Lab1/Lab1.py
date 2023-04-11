#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, 
#преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать 
#по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные 
#выражения использовать нельзя. Вещественные числа, заключенные в кавычки (все виды). Кавычки не выводятся. Целая часть числа выводится совами.
slovar = {".": '.', ",": ',', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'ноль'}
numbers = {str(x) for x in range(10)}
symbols = {'.', ',', ' ', '"', "'", "-"}

max_buffer_len = 100
buffer_len = 1

work_buffer = ""
number_flag = False
trash_flag = False
koll = 0
work_buffer_len = buffer_len

try:
    with open("text.txt", "r") as file:
        buffer = file.read(buffer_len)
        if not buffer:
            print("\nФайл test.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:
            if buffer == '.' or buffer == ',':
                koll += 1
            if koll == 1:
                if buffer >= '0' and buffer <= '9':
                    number_flag = True
                    work_buffer += slovar[int(buffer)]
            else:
                work_buffer += buffer
                if buffer >= '0' and buffer <= '9':
                    number_flag = True
                elif (buffer not in numbers) and (buffer not in symbols):
                    trash_flag = True

            if buffer.find(' ') >= 0 or buffer.find('"') >= 0 or buffer.find("'") >= 0:
                if number_flag and not (trash_flag) and koll == 1:
                    work_buffer = work_buffer
                    print(work_buffer)
                    number_flag = False
                trash_flag = False
                work_buffer = ""
                work_buffer_len = 0
                koll = 0
            buffer = file.read(buffer_len)
            work_buffer_len += buffer_len
            if work_buffer_len >= max_buffer_len and buffer.find('!') < 0 and buffer.find('?') < 0 and buffer.find('"') < 0 and buffer.find("'") < 0:
                print("\nФайл test.txt не содержит знаков, разделяющих числа, и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории проекта или переименуйте существующий *.txt файл.")
                buffer = ""

except FileNotFoundError:
    print("\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    
