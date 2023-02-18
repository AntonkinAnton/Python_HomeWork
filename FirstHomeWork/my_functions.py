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
        n//=10
    return sum

def end():
    import os
    print()
    os.system("pause")
