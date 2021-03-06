def find_contact(file_name, find_str):
    '''Для поиска контакта по элементу данных переданных в виде строки.
       Обработка данных. Вызов функции для
       вывода на печать найденного контакта(ов)'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.
    contact_number = 0 # Начальное значение переменной для формирования номера контакта.
    id_str = '' # Создаётся пустая строка.
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str_n = file_txt_r.readline() # Получение строки. 
        if data_str_n == '': # Если строка пустая то выход из цикла.
            if id_str.find('1') == -1: # Перед выходом из цикла проверяем строку 
                                       # id_str на наличиеидентификатора(ов) совпадений.
                                       # Если условие верно значит совпадений нет.
                print('                            ------------------') # Вывод на печать.
                print('                            | СОВПАДЕНИЙ НЕТ |') # Вывод на печать.
                print('                            ------------------') # Вывод на печать.
                file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла
        data_str = data_str_n.rstrip('\n') # Удаляет '\n' в конце строки.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.
        if data_str.find(find_str) != -1: # Если совпадения есть прибавляется к строке
                                          # id_str единица.
            id_str = id_str + '1' 
            print_contact(data_str, contact_number) # Функция вывода на печать.                 
        else:                             # Иначе прибавляется к строке id_str ноль.
            id_str = id_str + '0' 

