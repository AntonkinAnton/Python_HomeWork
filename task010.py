# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import my_functions
import random

my_functions.show_header('Программа показывает сколько нужно минимально перевернуть монеток,\n' + 'чтобы все были одинаково перевернуты'.center(56))

coins = my_functions.get_number('Введите число монет:')
print("\nПодбрасываем монеты...")

tail = 0
head = 0

for i in range(0, coins):

    current_coinup = random.randint(0,1)
    match (current_coinup):

        case 0:
            print("Решка!")
            tail +=1
            
        case 1:
            print("Орел!")
            head +=1

print(f'\nИтого:\n {head} Орлов\n {tail} Решек\n') 

match (head > tail):

    case True:
        print(f'Нужно перевернуть {tail} монет(-ы)\n') 

    case False:
        print(f'Нужно перевернуть {head} монет(-ы)\n')

my_functions.end()
