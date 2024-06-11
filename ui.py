from logger import input_data, print_data
from delit import  delit_data

def interface():
    print('Добрый день! Это бот справочник. \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление данных\n')
    command = int(input('Введите число '))
    print()

    while command != 1 and command != 2 and command != 3:
        print("Неправильный ввод")
        command = int(input('Введите число '))


    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delit_data()
