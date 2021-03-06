from datetime import datetime

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


     
    
    #---Блок кода для записи или дозаписи строковых данных в текстовый файл---
    file_txt_a = open('contact.txt', 'a') # Открытие текстового файла.
    file_txt_a.write(contact) # Запись содержимого переменной contact 
                              # в текстовый файл.
    file_txt_a.close() # Закрытие текстового файла.
