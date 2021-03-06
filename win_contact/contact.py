# Импортируется модуль os для удаления текстового файла.
import os
# Из модуля datetime импортируется класс datetime.
from datetime import datetime
# Импортируется модуль sys для выполнения выхода из программы.
import sys


def input_contact():
    '''Получение данных с клавиатуры и формирование
       строки для записи в текстовый файл.'''
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя (отчество): ')    
    address = input('Введите адрес: ')
    phone_number = input('Введите телефонный номер: ')
    email = input('Введите электронный адрес: ')
    add_inform = input('Дополнительная информация: ')
    # Получение даты и времени из ОС и присвоение
    # в виде строки переменной dt.
    dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    # Формирование строки с данными одного контакта. 
    contact = last_name + '&' + first_name + '&' + \
              address + '&' + phone_number + '&' + \
              email + '&' + add_inform + '&' + dt + '\n'
    return contact

def write_contact_txt(file_name, contact):
    '''Для записи контакта в текстовый файл. 
       Отрытие файла. Запись. Закрытие файла'''
    file_txt = open(file_name, 'a')
    file_txt.write(contact)
    file_txt.close()

def read_contact_txt(file_name):
    '''Для получения данных из текстового файла.
       Обработка данных. Вызов функции для
       вывода на печать всех контактов'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.        
    contact_number = 0 # Начальное значение переменной для формирования номера контакта.
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str_n = file_txt_r.readline() # Получение строки. 
        if data_str_n == '': # Если строка пустая то выход из цикла.
            file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.
        # Функция print_contact() принимает два аргумента.        
        print_contact(data_str_n, contact_number) # Функция вывода на печать.

def print_contact(data_str_n, contact_number):
    '''Получает строку контакта и его номер.
       Обработка данных. Вывод на печать контакта'''
    data_str = data_str_n.rstrip('\n') # Удаляет '\n' в конце строки.
    data_list = data_str.split('&')    # Полученная строка разделяется по символу &.
                                       # Формируется список data_list.
    contact_last_name = data_list[0]       # Получение фамилии.
    contact_first_name = data_list[1]      # Получение имени.
    contact_address = data_list[2]         # Получение адреса.   
    contact_phone_number = data_list[3]    # Получение номера телефона.
    contact_date_time_write = data_list[4] # Получение даты и времени записи контакта.
    contact_email = data_list[4]           # Получение электронного адреса.
    contact_add_inform = data_list[5]      # Получение дополнительной информации.
    contact_dt = data_list[6]              # Получение даты и времени записи контакта.
    #----------------------Вывод на печать контакта абонента------------------------
    pr_line_1 = f'-----------------------------------Контакт №{contact_number}'
    pr_line_2 = f'------{contact_dt}------'
    print(pr_line_1 + pr_line_2)
    print('Фамилия: ', contact_last_name)
    print('Имя (Отчество): ', contact_first_name)
    print('Адрес: ', contact_address)
    print('Номер телефона: ', contact_phone_number)
    print('Электронный адрес: ', contact_email)
    print('Дополнительная информация: ', contact_add_inform)

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

def del_contact(file_name, contact_number_for_del):
    '''Получает номер контакта. Удаляет контакт'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.
    contact_number = 0 # Начальное значение переменной для формирования номера контакта.
    list_for_new_txt = [] # Пустой список для формирования списка с контактами.
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str = file_txt_r.readline() # Получение строки контакта.
        if data_str == '': # Если строка пустая выход из цикла.
            file_txt_r.close() # Закрытие файла. 
            if contact_number_for_del > str(contact_number):
                print('Контакта с таким номером не существует')    
            break # Выход из цикла.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.
        if str(contact_number) == contact_number_for_del:
            continue # Если номер контакта совпадает с номером контакта для удаления
                     # эта строка контакта не добавляется в список list_for_new_txt.
                     # Следующий код этого цикла пропускается и переходит к
                     # следующей итерации цикла. 
        list_for_new_txt.append(data_str) # Добавляется в конец списка строка с контактом.

    os.remove(file_name) # Удаление текстового файла. Ниже будет создан новый текстовый файл.
                         # В этом файле будет отсутсвовать строка с удалённым контактом.

    while True: # Бесконечный цикл для выборки из списка list_for_new_txt строк с контактами
                # и записи их в текстовый файл.
        contact_for_wr = list_for_new_txt.pop(0) # Получает из списка элемент с индексом 0,
                                                 # присваивает его значение переменной
                                                 # contact_for_wr, а в списке 
                                                 # list_for_new_txt удаляет его.
        write_contact_txt(file_name, contact_for_wr) # Функция записи контакта в текстовый файл.
        if list_for_new_txt == []: # Если список пуст выход из цикла. 
            break # Выход из цикла.

# Переменной file_name присваивается строковое значение 
# с названием текстового файла. 
file_name = 'contact.txt' # Имя текстового файла.
pr_line = 2*'---------------------------------------' # Для оформления.

while True:
    print(pr_line) # Элемент оформления.
    # Переменной choice присваивается строка ('1' или '2' или '3' или '4' или '5')
    # для выбора действия в условии.
    choice  = input('Показать контакты- 1 Поиск- 2 Добавить контакт- 3 Удалить контакт- 4 Выход- 5: ')    
    if choice == '1':        
        print(pr_line) # Элемент оформления.
        try:
            # Вызов функции для чтения контактов из txt-файла и вывода на печать.
            read_contact_txt(file_name)
        except Exception: # Исключение.
            print('Список контактов пуст. Добавьте контакт.')     
    elif choice == '2':
        print(pr_line) # Элемент оформления.
        find_str = input('Введите информацию для поиска контакта: ')
        print(pr_line) # Элемент оформления.
        try:
            # Вызов функции для поиска контакта. 
            find_contact(file_name, find_str)
        except Exception: # Исключение.
            print('Список контактов пуст. Добавьте контакт.')            
    elif choice == '3':
        print(pr_line) # Элемент оформления.
        # Вызов функции для получения с клавиатуры нового контакта.
        # Строка с новым контактом присваивается переменной contact. 
        contact = input_contact()
        # Вызов функции для записи подготовленой строки контакта в txt-файл.
        write_contact_txt(file_name, contact)
    elif choice == '4':
        print(pr_line) # Элемент оформления.
        contact_number_for_del = input('Введите номер контакта для удаления: ')
        print(pr_line) # Элемент оформления.
        try:
            # Вызов функции для удаления контакта.
           del_contact(file_name, contact_number_for_del)
        except Exception: # Исключение.
            print('Список контактов пуст. Добавьте контакт.')        
    elif choice == '5':
        # Вызов функции exit() для выхода из программы.
        sys.exit()        
    else:
        print('Неверный символ для выбора действия. Введите 1, 2, 3, 4 или 5')

