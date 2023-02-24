# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import my_functions
import random

my_functions.show_header(
    "Программа показывает сколько раз встречается число в массиве")

list_size = my_functions.get_number("Введите размер массива")

start_range = my_functions.get_number(
    "Введите диапазон чисел для заполнения массива. От:")
end_range = my_functions.get_number("До:")

list = []

for i in range(0, list_size):
    list.append(random.randint(start_range, end_range))

print(f"\nВаш массив: {list}")

find_num = my_functions.get_number("\nВведите число для поиска:")
count = 0

for i in list:
    if i == find_num:
        count +=1

print(f"\nЧисло {find_num} встречается {count} раз")

my_functions.end()
