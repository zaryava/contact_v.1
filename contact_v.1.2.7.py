# Из модуля datetime импортируется класс datetime
from datetime import datetime
import sys

print('-----------------Выбери действие-----------------')
choice = input('Показать контакты- 1 Создать контакт- 2 Выход- 3: ')

if choice == '3':
    # Вызов функции exit() для выхода из программы.
    sys.exit()
elif choice == '2':
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')  
    address = input('Введите адрес: ')
    phone_number = input('Введите телефонный номер: ')
    email = input('Введите электронный адрес: ')
    add_inform = input('Дополнительная информация: ')
    # Получение даты и времени из ОС и присвоение в виде строки переменной dt
    dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    # Формирование строки с данными одного контакта.  
    contact = last_name + '&' + first_name + '&' + \
              address + '&' + phone_number + '&' + \
              email + '&' + add_inform + '&' + dt + '\n'
    #---Блок кода для записи или дозаписи строковых данных в текстовый файл---
    file_txt_a = open('contact.txt', 'a') # Открытие текстового файла.
    file_txt_a.write(contact) # Запись содержимого переменной contact 
                              # в текстовый файл.
    file_txt_a.close() # Закрытие текстового файла.
    #-------------------------------Конец блока-------------------------------
elif choice == '1':
    # Открытие файла для чтения данных.
    file_txt_r = open('contact.txt', 'r')
    # Начальное значение переменной для формирования номера контакта.
    contact_number = 0 
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str_n = file_txt_r.readline() # Получение строки. 
        if data_str_n == '': # Если строка пустая то выход из цикла.
            file_txt_r.close() # Закончились строки. Закрытие текстового файла.
            break
        data_str = data_str_n.rstrip('\n') # Удаляет '\n' в конце строки.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.
        # Строка разделяется по символу & и формируется список data_list.                    
        data_list = data_str.split('&')    
        contact_last_name = data_list[0]    # Получение фамилии.
        contact_first_name = data_list[1]   # Получение имени.
        contact_address = data_list[2]      # Получение адреса.    
        contact_phone_number = data_list[3] # Получение номера телефона.    
        contact_email = data_list[4]        # Получение электронного адреса.
        contact_add_inform = data_list[5]   # Получение дополнительной информации.
        contact_dt = data_list[6]           # Получение даты и времени записи контакта.
        # Вывод на печать данных контакта.
        print(f'------------------------Контакт №{contact_number}---------------------------')
        print('Фамилия: ', contact_last_name)
        print('Имя (Отчество): ', contact_first_name)
        print('Адрес: ', contact_address)
        print('Номер телефона: ', contact_phone_number)
        print('Электронный адрес: ', contact_email)
        print('Дополнительная информация: ', contact_add_inform)
        print('Дата и время записи: ', contact_dt)
else:
    print('Неверный символ для выбора действия.')


