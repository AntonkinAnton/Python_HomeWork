# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сборана них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import my_functions

my_functions.show_header("Крч, программа для нахождения большей суммы между тремя ближайшими элементами массива")

list = my_functions.make_random_list()

print(f"\nВаш массив:\n{list}")

max_summ = 0

for i in range(len(list)-2, -2, -1):
    print(list[i-1] + list[i] + list[i+1])
    if list[i-1] + list[i] + list[i+1] > max_summ:
        max_summ = list[i-1] + list[i] + list[i+1]

print(f"\nБольшая сумма трех ближайших элементов массива: {max_summ}")

my_functions.end()