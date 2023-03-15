from data_input import Choose_option, Header, Get_string
from os import system

def Replace_delete(old_line, new_line):
    system('cls||clear') 
    Header('Редактировать')
    
    print(old_line)
    choose = Choose_option("\n 1 - Изменить имя\n 2 - Изменить номер телефона\n 3 - Удалить запись\n", 1, 3)

    match choose:

        case 1:
            new_line[0] = Get_string("\nВведите новое имя: ")
            final_result = ' : '.join(new_line) + '\n'
        
        case 2:
            new_line[1] = Get_string("\nВведите новый номер телефона: ")
            final_result = ' : '.join(new_line) + '\n'

        case 3:
            final_result = ''
    
    with open('./base.txt', 'r', encoding='utf-8') as file:
        new_data = file.read().replace(old_line, final_result)

    with open('./base.txt', 'w', encoding='utf-8') as file:
        file.write(new_data)
    
    print("\nСделано!\n")
    
    system("pause")
    
