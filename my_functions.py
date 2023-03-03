def show_header(message):
    import os
    os.system('cls||clear')
    print("Антонкин Антон | Группа Программирование |11|4110| GeekBrains\n")
    print(f"{message}\n")


def get_number(message):
    while True:
        try:
            return int(input(f"{message}\n"))
        except:
            continue


def get_digitssum(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10

    return sum


def end():
    import os
    print()
    os.system("pause")


def is_equal_two_sides_sum(num):
    n = num
    count = 0

    while n != 0:
        n = int(n/10)
        count += 1

    second_half = int(num % (10**(int(count/2))))

    for i in range(0, int((count+1)/2)):
        num //= 10

    return get_digitssum(second_half) == get_digitssum(num)


def drawing_chocolate(raw, col):
    block = "▩ "
    print("\nВаш шоколад:")

    for i in range(0, raw):
        print(block*col)


def make_random_list():
    import random

    list_size = get_number("Введите размер массива")

    start_range = get_number(
        "Введите диапазон чисел для заполнения массива. От:")

    end_range = get_number("До:")

    list = []

    for i in range(0, list_size):
        list.append(random.randint(start_range, end_range))

    return list


def fill_list_random(size, start_range, end_range):
    import random

    list = []

    for i in range(0, size):
        list.append(random.randint(start_range, end_range))

    return list


def Degree_Recursion(a, b):

    if b == 1:
        return a
    
    if b == 0:
        return 1
    
    return a * Degree_Recursion(a, b - 1)

def Sum_Recursion(a, b):

    if b == 0:
        return a
    
    return Sum_Recursion(a, b - 1) + 1