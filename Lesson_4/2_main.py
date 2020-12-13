""""""""""""""""""""""""""""""
""" ИМПОРТ  СВОИХ  МОДУЛЕЙ """
""""""""""""""""""""""""""""""
# from 2_my_module
# from Lesson_4 import my_module

# print(my_module)
# print(my_module.div_num)
# print(my_module.div_num(10, 2))


""""""""""""""""""""""""""""""""""""
""" ЗАПУСК СКРИПТА С ПАРАМЕТРАМИ """
""""""""""""""""""""""""""""""""""""
import sys

# Modify Run configuration -> Parameters
print(sys.argv)

try:
    filename, a, b, c = sys.argv
except ValueError as error:
    print(f'Error is {error}\nInvalid args')
    exit()


def division(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return a / b + c


print(division(a, b, c))
