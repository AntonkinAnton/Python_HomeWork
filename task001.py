# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)

import my_functions

my_functions.show_header("Программа показывает сумму всех цифр в числе")

number = my_functions.get_number("Введите число:")

print(f"\nСумма цифр числа {number} -> {my_functions.get_digitssum(number)}")

my_functions.end()