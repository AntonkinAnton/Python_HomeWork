
def OutputAll():

    with open('./Phonebook/file.txt', 'r', encoding='utf-8') as file:
        place = 0          # переменная для вывода номера строки
        for line in file:
            place += 1
            print(f"{place}. {line}")
       

            

