# Из модуля datetime импортируется класс datetime
#from datetime import datetime

#last_name = input('Введите фамилию: ')
#first_name = input('Введите имя: ')  
#address = input('Введите адрес: ')
#phone_number = input('Введите телефонный номер: ')
#email = input('Введите электронный адрес: ')
#add_inform = input('Дополнительная информация: ')

# Получение даты и времени из ОС и присвоение в виде строки переменной dt
#dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

# Формирование строки с данными одного контакта.  
#contact = last_name + '&' + first_name + '&' + \
#          address + '&' + phone_number + '&' + \
#          email + '&' + add_inform + '&' + dt + '\n'

# Вывод на печать строковых данных подготовленных
# для записи в текстовый файл.
#print(contact) 

#---Блок кода для записи или дозаписи строковых данных в текстовый файл---
#
#file_txt_a = open('contact.txt', 'a') # Открытие текстового файла.
#file_txt_a.write(contact) # Запись содержимого переменной contact 
                          # в текстовый файл.
#file_txt_a.close() # Закрытие текстового файла.
#
#-------------------------------Конец блока-------------------------------

#--------Блок кода для чтения строковых данных из текстового файла--------
#
file_txt_r = open('contact.txt', 'r') # Открытие текстового файла.
data1 = file_txt_r.readline() # Считывание первой строки данных из файла.
data2 = file_txt_r.readline() # Считывание второй строки данных из файла.
data3 = file_txt_r.readline() # Считывание третьей строки данных из файла.
file_txt_r.close() # Закрытие текстового файла.
#
#-------------------------------Конец блока-------------------------------

print(data1) # Вывод на печать данных первого контакта.
print(data2) # Вывод на печать данных второго контакта.
print(data3) # Вывод на печать данных третьего контакта.



