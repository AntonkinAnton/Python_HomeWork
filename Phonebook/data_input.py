from os import system

def Header(message = "\n"):
    print('Телефонный справочник'.center(70, '='), '\n')
    print(message.center(70, '='), '\n')

def Choose_option(message, first_option = 0, last_option = 1):
    input_data = first_option-1
    while input_data < first_option or input_data > last_option:
        try:
            input_data = int(input(f"{message}\n"))
        except:
            continue

    return input_data

def Get_string(message):
    while True:
        get_string = input(f"{message}")

        if get_string == '':
            print('Поле не может быть пустым!')
        else:
            return get_string
        
def Get_num(message):
    while True:
        get_string = input(f"{message}")
        try:
            int(get_string)
            return get_string
        except:
            print('Введены не цифры!\n')
            continue

def Add_entry():
    system('cls||clear') 
    Header('Добавить запись')

    name = Get_string('\nВведите имя:\n')
    phone_number = Get_string('\nВведите номер телефона:\n')

    with open('./base.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'{name} : {phone_number}\n')

    print('\nДобавлено!\n')

    system("pause")


