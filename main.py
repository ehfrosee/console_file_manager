from victory import victory_game
from bank_account import bank_account
from os_functions import list_dir, mk_dir, rm_dir, file_copy, sys_info, program_author
menu = [
    '1 - создать папку',
    '2 - удалить(файл / папку)',
    '3 - копировать(файл / папку)',
    '4 - просмотр содержимого рабочей директории',
    '5 - посмотреть только папки',
    '6 - посмотреть только файлы',
    '7 - просмотр информации об операционной системе',
    '8 - создатель программы',
    '9 - играть в викторину',
    '10 - мой банковский счет',
    '11 - смена рабочей директории(*необязательный пункт)',
    '12 - выход'
    ]

while True:
    print("\n" + "*"*10)
    for menu_item_string in menu:
        print(menu_item_string)
    menu_item = input('Выберите пункт меню: ')
    match menu_item:
        case '1':
            dir_name = input("Введите имя создаваемой папки или файла: ")
            mk_dir(dir_name)
        case '2':
            dir_name = input("Введите имя удаляемой папки или файла: ")
            rm_dir(dir_name)
        case '3':
            filename = input("Введите имя копируемой папки или файла: ")
            newname = input("Введите новое имя: ")
            file_copy(filename, newname)
        case '4':
            list_dir()
        case '5':
            pass
        case '6':
            pass
        case '7':
            sys_info()
        case '8':
            pass
        case '9':
            victory_game()
        case '10':
            bank_account()
        case '11':
            program_author()
        case '12':
            break
        case _:
            print('Неверный пункт меню')
