from logger import print_data

def delit_data():
    spisok_1, spisok_2 = print_data()
    print_data()
    delit_num = int(input('Введите из какого файла необходимо удалить ? '))
    print()

    while delit_num != 1 and delit_num != 2:
        print("Неправильный ввод")
        delit_num = int(input('Введите число '))

##filename = "filewithcontents.csv"
# opening the file with w+ mode truncates the file
#f = open(filename, "w+")
#f.close()


    if delit_num == 1:
        print(*spisok_1)
        del_num1 = int(input('Выберите какую запись удалить целиком '))
        spisok_1.pop(del_num1-1)
        print(spisok_1)
        with open ('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in spisok_1:
                f.write(i)
        print(spisok_1)
        
    elif delit_num == 2:
        print(*spisok_2)
        del_num2 = int(input('Выберите какую запись удалить целиком '))
        spisok_2.pop(del_num2-1)
        print(spisok_2)
        with open ('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in spisok_2:
                f.write(i)
        print(spisok_2)

#delit_data()