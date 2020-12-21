# Импортируется модуль sys для выполнения выхода из программы.
import sys
# Из модуля defcont импортируются функции.
from defcont import input_contact, read_contact_txt, write_contact_txt, find_contact, del_contact 

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

