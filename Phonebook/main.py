from data_input import*
from data_output import*
from data_search import*
from data_clear import*
from os import system

system('cls||clear')

file = open('./base.txt', 'a', encoding='utf-8')    #для создания файла базы, если его нет
file.close()

while True:

    Header('Главное меню')

    choice = Choose_option('Введите нужное действие: \n\
       \n 1 - Добавить в справочник \
        \n 2 - Показать весь справочник \
         \n 3 - Поиск и редактирование \
          \n 4 - Очистить справочник \
           \n\n 0 - Выход \n', 0, 4)
    
    match choice: 
        
        case 1: 
            Add_entry()

        case 2: 
            OutputAll()

        case 3:           
            Search()

        case 4:           
            Clear_base()

        case 0: 
            print("\nДо скорой встречи!\n")
            system("pause")
            break

    system('cls||clear') 

    

