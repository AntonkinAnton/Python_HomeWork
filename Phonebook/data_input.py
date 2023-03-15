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

def Add_entry():
    system('cls||clear') 
    Header('Добавить запись')

    name = Get_string('\nВведите имя: ')
    phone_number = Get_string('\nВведите номер телефона: ')

    with open('./base.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'{name} : {phone_number}\n')

    print('\nДобавлено!\n')

    system("pause")


