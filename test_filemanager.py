from os_functions import mk_dir, list_dir_only,  rm_dir, rm_file, file_copy, list_file_only
import os

def test_dir():
    #тестирование функций работы с папками
    list_dir_only()
    dir_name = "new_folder"
    mk_dir(dir_name)
    dir_list = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name))]
    list_dir_only()
    assert dir_name in dir_list
    rm_dir(dir_name)
    dir_list = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name))]
    list_dir_only()
    assert dir_name not in dir_list
    print('dir test OK')

def file_test():
    filename = 'test_filemanager.py'
    newname = 'test_filemanager_copy.py'
    list_file_only()
    file_copy(filename, newname)
    file_list = [name for name in os.listdir('.') if os.path.isfile(os.path.join('.', name))]
    assert newname in file_list
    rm_file(newname)
    file_list = [name for name in os.listdir('.') if os.path.isfile(os.path.join('.', name))]
    assert newname not in file_list
    list_file_only()
    print('file test OK')

if __name__ == "__main__":
    test_dir()
    file_test()
