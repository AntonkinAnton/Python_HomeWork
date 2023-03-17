from os import system
from data_input import Choose_option, Header, Get_num
from data_replace import Replace_delete

def Select_data():
    system('cls||clear')
    Header('Выборка номеров по последним цифрам')

    with open('./base.txt', 'r', encoding='utf-8') as file:
        whole_list = file.readlines()

        if len(whole_list) == 0:  #если справочник пуст
            print('Нет записей!\n')
            system("pause")
            return
        
        num = Get_num('Введите последние цифры номера для поиска:\n')
        print()
        
        res = ''
        place = 0
        found_list_index = []

        for i in range(len(whole_list)):
            line = whole_list[i].strip('\n')

            for j in range (len(num)):
                res += line[len(line)-1-j]
            if res[::-1] == num:
                place += 1
                print(f"{place}. {whole_list[i]}")
                found_list_index.append(i)
            res = ''

        if place == 0:
            print('Нет совпадений!\n')
            system("pause")
            return
        
        choose_result = Choose_option("Для изменения введите порядковый номер записи:\n 0 - Выйти в главное меню\n", 0, place)

        if choose_result == 0:   
            return
        
        old_line = whole_list[found_list_index[choose_result-1]]
        new_line = whole_list[found_list_index[choose_result-1]].strip('\n').split(' : ')  
        
        Replace_delete(old_line, new_line)

