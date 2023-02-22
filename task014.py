# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import my_functions

my_functions.show_header("Программа показывает все степени двойки до N")

N = my_functions.get_number("Введите N:")
i = 2
print(f"\nСтепени двойки до {N}:")

while i < N:
    print(i)
    i *= 2

my_functions.end()