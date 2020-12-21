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



