
def Search(data):
     with open('./Phonebook/file.txt', 'r', encoding='utf-8') as file:
        find_flag = False
        found_list_index = []
        place = 0
        whole_list = file.readlines()

        for i in range(len(whole_list)):
            if data.lower() in whole_list[i].lower():
                place += 1
                print(f"{place}. {whole_list[i]}")
                found_list_index.append(i)
                # found_list.append(line.strip('\n').split(' : '))
                find_flag = True
                
        if find_flag == False:     
            print('\nНе найдено!\n')
        print(found_list_index)

        