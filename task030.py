# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import my_functions

my_functions.show_header("Программа показывает арифметическую прогрессию")

first_num = my_functions.get_number("Введите начальное число прогрессии:")

step = my_functions.get_number("Введите шаг прогрессии:")

lenght = my_functions.get_number("Введите длину прогрессии:")

list = []

# for i in range(lenght):     # Решение здорового человека
#     list.append(first_num)
#     first_num += step

for i in range(lenght):            # Решение курильщика
    list.append(first_num + i * 2)


print("\nВаша прогрессия: ", list)

my_functions.end()
