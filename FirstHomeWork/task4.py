# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

import my_functions

my_functions.show_header(
    "Программа показывает можно ли отломить заданную дольку по прямой от куска шоколада")

raws = my_functions.get_number("Задайте длину шоколада:")

columns = my_functions.get_number("Задайте ширину шоколада:")

my_functions.drawing_chocolate(raws, columns)

piece = my_functions.get_number("\nВведите размер кусочка в дольках:")

real = piece % raws == 0 or piece % columns == 0

if real:
    print(f"\nКусок размером {piece} долек ВЗМОЖНО отломить по прямой линии")
else:
    print(f"\nКусок размером {piece} долек НЕВОЗМОЖНО отломить по прямой линии")

my_functions.end()