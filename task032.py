# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from my_functions import fill_list_random, end, get_number, show_header

show_header("Программа показывает индексы чисел, которые лежат в заданном диапазоне")

list_range = [get_number("Введите диапазон от:"), get_number("До:")]

array = fill_list_random(10, 0, 20)
print(f"\nВаш массив:\n{array}")
result_list = []

for i in range(len(array)):
    if list_range[0] < array[i] < list_range[1]:
        result_list.append(i)

print(f"\nИндексы элементов, которые лежат в диапазоне {list_range[0]}-{list_range[1]}:\n{result_list}")

end()