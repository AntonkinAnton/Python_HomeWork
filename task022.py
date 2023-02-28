# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import my_functions

my_functions.show_header("Программа показывает совпадения элементов в двух списках по возрастанию")

first_list_size = my_functions.get_number("Введите размер первого массива:")

second_list_size = my_functions.get_number("Введите размер второго массива:")

(start_rand_range, end_rand_range) = \
    my_functions.get_number("Введите диапазон чисел для заполнения массивов. От:"), \
    my_functions.get_number("До:")

first_list = my_functions.fill_list_random(first_list_size, start_rand_range, end_rand_range)

second_list = my_functions.fill_list_random(second_list_size, start_rand_range, end_rand_range)

print(f"\nВаши массивы:\n{first_list}\n{second_list}")

q1 = set(first_list)
q2 = set(second_list)

print("\nОдинаковые элементы в порядке возрастания:")
print(sorted(q1.intersection(q2)))

my_functions.end()