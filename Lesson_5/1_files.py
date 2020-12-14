""""""""""""""""""""""""
""" РАБОТА С ФАЙЛАМИ """
""""""""""""""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html """
# my_file = open('data.txt')
# print(my_file)
#
# print(my_file.read())
#
# my_file.close()


""" КОГДА ФАЙЛА НЕТ """
# my_file = open('data111.txt')

# перехват ошибки, но плохой
# try:
#     my_file = open('data11.txt')
#     for line in my_file.readline():
#         print(line)
# except IOError:
#     print('Error')
# finally:
#     my_file.close()


""" АБСОЛЮТНЫЙ ПУТЬ """
# my_file = open('/home/julia/PycharmProjects/geekbrains_python/Lesson_5/data.txt')
# my_file = open('C:\temp\file.txt')
# my_file = open(r'C:\\temp\\file.txt')  # отмена экранирование
# my_file = open(r'C:\temp\file.txt')  # сырая строка


""" ЧТЕНИЕ ФАЙЛА """
my_file = open('data.txt')

# print(my_file.readline())
# print(my_file.readlines())
# for line in my_file.readlines():
#     print(line.replace('\n', ''))


# print(my_file.read())  # удобно, но возвращается одна строка, плюс память может закончиться
# print(my_file.read(5))

""" УКАЗАТЕЛИ В ФАЙЛЕ """
# tell() - Определяет, в скольких байтах от начала файла находится указатель
print(my_file.read(3))
print(my_file.tell())
print(my_file.read(3))
print(my_file.tell())
print(my_file.read(5))
print(my_file.tell())
print(my_file.read())
print(my_file.tell())

print(my_file.read())

# seek() - Позволяет выполнить переход на нужную позицию
my_file.seek(0)
print(my_file.tell())
print(my_file.read())
print(my_file.tell())
my_file.seek(5)
print(my_file.tell())

my_file.close()


""" ЗАПИСЬ В ФАЙЛ """
# my_file = open('data.txt')
#
# if my_file.writable():
#     my_file.write('Update')
# else:
#     print('Invalid')
#
# my_file.close()


""" МОДИФИКАТОР НА ЗАПИСЬ """
# my_file = open('data.txt', mode='w')
#
# if my_file.writable():
#     my_file.write('Update')
#
#     strings = ['Anna', 'John']
#     # strings = ['Anna\n', 'John\n']
#     # '\n'.join(strings)
#     my_file.writelines(strings)
# else:
#     print('Invalid')


""" ПАРАМЕТРЫ ФАЙЛОВОГО ОБЪЕКТА """
# print(my_file.closed, my_file.name, my_file.mode)
# my_file.close()
# print(my_file.closed, my_file.name, my_file.mode)
