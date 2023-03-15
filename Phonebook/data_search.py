from data_input import Choose_option, Header
from data_replace import Replace_delete
from os import system


def Search():
    system('cls||clear') 
    Header('Поиск и редактирование')
    
    with open('./base.txt', 'r', encoding='utf-8') as file:
        whole_list = file.readlines()    # помещаем все строки файла в отдельную переменную
        found_list_index = []          # для записи индексов найденных строк
        place = 0                    # переменная для вывода номера строки

        if len(whole_list) == 0:  #если справочник пуст
            print('Нет записей!\n')
            system("pause")
            return
        
        data = input('Введите данные для поиска: ')
        print()

        for i in range(len(whole_list)):
            if data.lower() in whole_list[i].lower():
                place += 1
                print(f"{place}. {whole_list[i]}")
                found_list_index.append(i)

        if place == 0:
            print('\nНе найдено!\n')
            system("pause")
            return

        choose_result = Choose_option("Для изменения введите порядковый номер записи:\n 0 - Выйти в главное меню\n", 0, place)

        if choose_result == 0:   
            return
        
        #делим строку на список в формате ['имя','тел']:
        old_line = whole_list[found_list_index[choose_result-1]]
        new_line = whole_list[found_list_index[choose_result-1]].strip('\n').split(' : ')  
        

        Replace_delete(old_line, new_line)  #переходим в replacer


    
