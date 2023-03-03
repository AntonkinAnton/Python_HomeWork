# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

import my_functions

my_functions.show_header("Программа возводит введенное число в введеную степень")

num = my_functions.get_number("Введите число:")

degree = my_functions.get_number("Введите степень:")

print(f'\nЧисло {num} в степени {degree} = {my_functions.Degree_Recursion(num, degree)}')

my_functions.end()
