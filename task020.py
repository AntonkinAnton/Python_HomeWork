# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
import my_functions

list_of_letters = [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
                   ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
                   ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
                   ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
                   ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
                   ['J', 'X', 'Ш', 'Э', 'Ю'],
                   ['Q', 'Z', 'Ф', 'Щ', 'Ъ']]

list_of_points = [1, 2, 3, 4, 5, 8, 10]

scrubble_dict = dict()

for i in range (0,len(list_of_letters)):

    for j in list_of_letters[i]:
        scrubble_dict[j] = list_of_points[i]

my_functions.show_header("Сыграем в Scrabble?")

input_word = input("Введите слово:\n").upper()

result_sum = 0

for i in input_word:
    if i in scrubble_dict:
        result_sum += scrubble_dict[i]

# -------------------------решение, когда ключ - очки-----------
# i = 0
# for j in list_of_points:
#     scrubble_dict[j] = list_of_letters[i]
#     i += 1

# for i in input_word:
#     for j in scrubble_dict:
#         if i in scrubble_dict[j]:
#             result_sum += j

print("\nВаш результат: ", result_sum)

my_functions.end()
