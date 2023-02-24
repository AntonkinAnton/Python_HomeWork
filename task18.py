# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import my_functions

my_functions.show_header("Программа показывает ближайший элемент к введенному числу")

list = my_functions.make_random_list()

print(f"\nВаш массив: {list}")

find_num = my_functions.get_number("\nВведите число для поиска:")

nearest = 2147483647   #макс знач int
nearest_index = None

for i in range(0, len(list)):
    if abs(list[i] - find_num) < nearest:
        nearest = abs(list[i] - find_num)
        nearest_index = i

print(f"\nБлижайшее число к {find_num} >>> {list[nearest_index]} ({nearest_index + 1} элемент массива)")

my_functions.end()
