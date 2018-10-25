# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys
path_dir =[('dir_' + str(i + 1)) for  i in range(9)]
 
def make_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(dir_path)
        print('Вы успешно удалили ' + paths)
    except:
        print('Не возможно создать' + dir_path + ' - такая директория уже есть')
        
#def remove_dir(path_to_remove):
#    try:
#        os.removedirs(path_to_remove)
#        print('Вы успешно удалили ' + path_to_remove)
#    except (TypeError, FileNotFoundError):
#        print('Не возможно удалить')

 
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
 
 
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
 
def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)
 
 
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
        print('Вы успешно удалили ' + dir_path)
    except:
        print(dir_path + ' - такой директории нет')

 
def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print('Вы успешно перешли в ' + os.getcwd())
    except:
        print('Не возможно удалить' + dir_path + ' - такой директории нет')

 



