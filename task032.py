# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import my_functions

my_functions.show_header("Программа показывает индексы чисел, которые лежат в заданном диапазоне")

list_range = [my_functions.get_number("Введите диапазон от:"), my_functions.get_number("До:")]

array = my_functions.fill_list_random(10, 0, 20)
print(f"\nВаш массив:\n{array}")
result_list = []

for i in range(len(array)):
    if list_range[0] < array[i] < list_range[1]:
        result_list.append(i)

print(f"\nИндексы элементов, которые лежат в диапазоне {list_range[0]}-{list_range[1]}:\n{result_list}")

my_functions.end()