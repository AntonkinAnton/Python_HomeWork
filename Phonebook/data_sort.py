from os import system
from data_input import Choose_option, Header

def Sort_data():
    system('cls||clear')
    Header('Сортировка справочника')

    with open('./base.txt', 'r', encoding='utf-8') as file:
        whole_list = file.readlines()

        if len(whole_list) == 0:  #если справочник пуст
            print('Нет записей!\n')
            system("pause")
            return
        
        choose = Choose_option("Выберите порядок сортировки:\n 1 - А >>> Я\n 2 - Я >>> А\n 0 - Выйти в главное меню\n", 0, 2)

        match choose:

            case 1:
                whole_list.sort()

            case 2:
                whole_list.sort()
                whole_list.reverse()

            case 0:
                return
            
    with open('./base.txt', 'w', encoding='utf-8') as file:

        file.writelines(whole_list)
        print("\nСделано!\n")
        system("pause")
        
