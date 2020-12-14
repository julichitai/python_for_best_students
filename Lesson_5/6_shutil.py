""""""""""""""""""""""""
""" РАБОТА С  SHUTIL """
""""""""""""""""""""""""
""" https://pythonworld.ru/moduli/modul-shutil.html """
import shutil


""" КОПИРОВАНИЕ """
shutil.copy('model.json', './test_dir/copied.json')
shutil.copy('model.json', './test_dir')

shutil.copyfile('model.json', './test_dir/copied2.json')


with open('./dataset/pigeons/pigeons_1.jpg', 'rb') as fsrc:
    with open('./test_dir/pigeon.jpg', 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)


# shutil.copytree('./dataset', './new_dataset')


""" ПЕРЕМЕЩЕНИЕ """
# shutil.move('./new_dataset', './test_dir')


""" УДАЛЕНИЕ """
# shutil.rmtree('./test_dir')

