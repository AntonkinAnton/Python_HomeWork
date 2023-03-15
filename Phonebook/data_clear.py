from data_input import Choose_option, Header
from os import system

def Clear_base():
    system('cls||clear') 
    Header("Очистить справочник")
    choose = Choose_option("Вы уверены? Данное действие удалит ВСЕ записи справочника:\n 1 - Да\n 0 - Нет\n", 0, 1)

    if choose == 0:
        return
    
    file = open('./base.txt', 'w', encoding='utf-8')
    file.write('')
    file.close
    print('\nДанные удалены\n')
    system("pause")

    
