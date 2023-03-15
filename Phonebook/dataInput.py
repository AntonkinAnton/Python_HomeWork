
def Input(data, number):

    with open('./Phonebook/file.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'{data} : {number}')
    print('\nДобавлено\n')
       


