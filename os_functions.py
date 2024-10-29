import random
import os
import sys
import shutil

# os - основные функции

# список файлов и папок
def list_dir():
    print(os.listdir())

def mk_dir(dirname):
    # проверка на существование
    if not os.path.exists(dirname):
        # сздать папку передаем путь
        os.mkdir(dirname)
        print(f'Папка {dirname} создана')
    else:
        print(f'Папка с именем {dirname} существует')

def rm_dir(dirname):
    # удалить папку
    if os.path.exists(dirname):
        os.rmdir(dirname)
        print(f'Папка {dirname} удалена')
    else:
        print(f'Папкаи с именем {dirname} не существует')

# shutil
def file_copy(filename, newname):
    shutil.copy(filename, newname)

# sys
def sys_info():
    print(sys.platform)

def program_author():
    print('Автор программы: Эфрос Евгений Евгеньевич')


# # путь до текущей папки
# print(os.getcwd())
# # соединение путей
# path = os.path.join(os.getcwd(), 'main', 'other', 'file.txt')
# print(path)
#
# # Это пути где питон ищет файлы
# print(sys.path)
#
# # sys.path.remove('/home/dante/Документы/NU/NU5Модули/Задание дз/lesson5modules')
# # sys.path.remove('/home/dante/Документы/NU/NU5Модули/Задание дз/lesson5modules')
# print(sys.path)
# sys.path.append('/home/dante/')
# print(sys.path)
# import hello
#
# print(sys.executable)

# import random
# import math
# import functools
# import glob