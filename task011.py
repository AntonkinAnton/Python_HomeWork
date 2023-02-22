# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import my_functions

my_functions.show_header(
    "Программа находит два числа, если известны их сумма и произведение")

sum = my_functions.get_number("Введите сумму двух чисел:")

mult = my_functions.get_number("Введите произведение двух чисел:")

while (True):
    choice = my_functions.get_number("\nВыберете способ решения задачи:\n1 - через Дискриминант математически (любые натуральные числа)" +
                                     "\n2 - перебором (проверка чисел до 1000)")
    match(choice):
        case 1:
            import math
            D = (sum**2) - 4 * mult * 1
            if D < 0:
                print("\nНет подходящих чисел!")
            else:
                x = (sum + math.sqrt(D))/2
                y = sum - x
                if (float(x) == int(x)):
                    print(f"\nВаши числа: {int(x)} и {int(y)}")
                else:
                    print("\nЧисла не являются натуральными")
            break
        case 2:
            x = 0
            y = None
            while x < 1000:
                if ((x**2)-(sum*x) + mult == 0):
                    y = sum - x
                    print(f"\nВаши числа: {int(x)} и {int(y)}")
                    break
                else:
                    x += 1
            else:
                print("\nНет подходящих чисел, либо числа больше 1000")
            break
        case _:
            continue

my_functions.end()
