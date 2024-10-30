from victory import victory_game
from bank_account import bank_account
from os_functions import list_dir, mk_dir, rm_dir, file_copy, sys_info, program_author, rm_file, list_dir_only, list_file_only
menu = [
    '1 - создать папку',
    '2 - удалить папку',
    '3 - удалить файл',
    '4 - копировать(файл / папку)',
    '5 - просмотр содержимого рабочей директории',
    '6 - посмотреть только папки',
    '7 - посмотреть только файлы',
    '8 - просмотр информации об операционной системе',
    '9 - создатель программы',
    '10 - играть в викторину',
    '11 - мой банковский счет',
    '12 - смена рабочей директории(*необязательный пункт)',
    '13 - выход'
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
            dir_name = input("Введите имя удаляемой папки: ")
            rm_dir(dir_name)
        case '3':
            file_name = input("Введите имя удаляемого файла: ")
            rm_file(file_name)
        case '4':
            filename = input("Введите имя копируемой папки или файла: ")
            newname = input("Введите новое имя: ")
            file_copy(filename, newname)
        case '5':
            list_dir()
        case '6':
            list_dir_only()
        case '7':
            list_file_only()
        case '8':
            sys_info()
        case '9':
            pass
        case '10':
            victory_game()
        case '11':
            bank_account()
        case '12':
            program_author()
        case '13':
            break
        case _:
            print('Неверный пункт меню')
