# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import my_functions

my_functions.show_header("Программа суммирует два чилса через рекурсию")

first_num = my_functions.get_number("Введите первое число:")

second_num = my_functions.get_number("Введите второе число:")

print(f"\n{first_num} + {second_num} = {my_functions.Sum_Recursion(first_num, second_num)}")

my_functions.end()
