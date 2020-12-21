def write_contact_txt(file_name, contact):
    '''Для записи контакта в текстовый файл. 
       Отрытие файла. Запись. Закрытие файла'''
    file_txt = open(file_name, 'a')
    file_txt.write(contact)
    file_txt.close()

