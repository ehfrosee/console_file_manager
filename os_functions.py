import random
import os
import sys
import shutil


# os - основные функции
# Добавление названия функции
def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print(f'**{f.__name__}**')
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 10)
        return result

    # возвращается функция inner с новым поведением
    return inner

# список файлов и папок
@add_separators
def list_dir(directory='.'):
    # Вывод папок
    dir_list = os.listdir(directory)
    print(dir_list)


@add_separators
def list_dir_only(directory='.'):
    # Вывод папок
    # dir_list = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    # dir_list = (name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)))
    dir_list = filter(lambda name: os.path.isdir(os.path.join(directory, name)), os.listdir(directory))
    print(list(dir_list))


@add_separators
def list_file_only(directory='.'):
    # Вывод файлов
    # file_list = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
    # file_list = (name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name)))
    file_list = filter(lambda name: os.path.isfile(os.path.join(directory, name)), os.listdir(directory))
    print(list(file_list))


@add_separators
def mk_dir(dirname):
    # проверка на существование
    #    if not os.path.exists(dirname):
    try:
        # сздать папку передаем путь
        os.mkdir(dirname)
        print(f'Папка {dirname} создана')
    except FileExistsError:
        #    else:
        print(f'Папка с именем {dirname} существует')
    except OSError as e:
        print(f"Ошибка при создании директории: {e}")


@add_separators
def rm_dir(dirname):
    # удалить папку
    try:
        os.rmdir(dirname)
        print(f'Папка {dirname} удалена')
    except FileNotFoundError:
        print(f'Папка с именем {dirname} не существует')
    except OSError:
        print(f'Папка с именем {dirname} не пустая')


@add_separators
def rm_file(filename):
    # Удалить файл
    try:
        os.remove(filename)
        print(f'Файл {filename} удален')
    except FileNotFoundError:
        print(f'Файл с именем {filename} не существует')
    except OSError:
        print(f'для удаления {filename} выберите пункт "Удалить папку"')


# shutil
@add_separators
def file_copy(filename, newname):
    shutil.copy(filename, newname)


# sys
@add_separators
def sys_info():
    print(sys.platform)


@add_separators
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
