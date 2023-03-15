from data_input import Choose_option, Header
from data_replace import Replace_delete
from os import system

def OutputAll():
    system('cls||clear') 
    Header('Весь справочник')
    
    with open('./base.txt', 'r', encoding='utf-8') as file:
        place = 0            # переменная для вывода номера строки
        whole_list = file.readlines()

        if len(whole_list) == 0:  #если справочник пуст
            print('Нет записей!\n')
            system("pause")
            return

        for i in range(len(whole_list)):   #печатаем построчно базу
            place += 1
            print(f"{place}. {whole_list[i]}")

        choose_result = Choose_option("Для изменения введите порядковый номер записи:\n 0 - Выйти в главное меню\n", 0, place)

        if choose_result == 0:
            return
        
        old_line = whole_list[choose_result-1]
        new_line = whole_list[choose_result-1].strip('\n').split(' : ')

        Replace_delete(old_line, new_line)  #переходим в replacer

            

