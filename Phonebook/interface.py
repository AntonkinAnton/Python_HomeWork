from dataInput import*
from dataOutput import*
from searchChange import*
from os import system
system('cls||clear')

while True:

    choice = input('Введите нужное действие: \n 1 - Добавить в справочник \
        \n 2 - Показать весь справочник \n 3 - Поиск и замена \n 4 - Выход \n')
    
    match choice: 
        
        case '1': 
            system('cls||clear')
            Input(input('\nВведите имя: '), input('Введите номер: '))

        case '2': 
            system('cls||clear')
            OutputAll()

        case '3':  
            system('cls||clear')          
            Search(input('Введите данные для поиска: '))

        case '4': 
            print("До скорой встречи!")
            break

    

