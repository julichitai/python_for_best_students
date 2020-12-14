""""""""""""""""""""
""" РАБОТА  С OS """
""""""""""""""""""""
""" https://pythonworld.ru/moduli/modul-os.html """
""" https://pythonworld.ru/moduli/modul-os-path.html """
import os


""" REMOVE, RENAME, PATH, LISTDIR """
# os.rename('new.txt', 'delete.txt')
if os.path.exists('delete.txt'):
    os.remove('delete.txt')


files = os.listdir()
# files = os.listdir('../')
print(files)


print('dir', [i for i in files if os.path.isdir(i)])
print('file', [i for i in files if os.path.isfile(i)])


print('basename', os.path.basename('Lesson_5/data.txt'))
print('split', os.path.split('Lesson_5/data.txt'))
print('split', os.path.split('geekbrains_python/Lesson_5/data.txt'))


""" ЕСЛИ НАДО ПОЛУЧИТЬ ВСЕ ФАЙЛЫ В ЗАДАННЫХ ДИРЕКТОРИЯХ """
files = []
root_dir = './dataset'
for dir in os.listdir(root_dir):
    dir_path = os.path.join(root_dir, dir)
    for path in os.listdir(dir_path):
        whole_path = os.path.join(dir_path, path)
        files.append(whole_path)
print(len(files), files)


""" ЧЕРЕЗ COMPREHENSION """
dirs = [os.path.join(root_dir, directory) for directory in os.listdir(root_dir)]
print(dirs)
files = [os.path.join(root_dir, file) for directory in dirs for file in os.listdir(directory)]
print(len(files), files)


""""""""""""""""""""""""
""" РАБОТА С PATHLIB """
""""""""""""""""""""""""
from pathlib import Path

root_path = Path('./dataset')
dirs = [directory for directory in root_path.iterdir() if directory.is_dir()]
print(dirs)
files = [file for directory in dirs for file in directory.glob('*.jpg')]
print(len(files), files)


""" ОТЛИЧИЯ OS ОТ PATHLIB """
path1 = 'Lesson_5'
path2 = '/dataset'
path3 = 'cat'
path4 = 'cat_1.jpg'
path = os.path.join(path1, path2, path3, path4)
print(type(path), path)


path1 = Path('Lesson_5')
path2 = Path('/dataset')
path3 = Path('cat')
path4 = Path('cat_1.jpg')
path = path1 / path2 / path3 / path4
print(type(path), path)

print(files[0].parts)




