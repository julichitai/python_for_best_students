""""""""""""""""""""""""
""" КОНСТРУКЦИЯ WITH """
" контекстный менеджер "
""""""""""""""""""""""""
""" https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html """
# with open('data.txt') as file:
#     print(file.readline())
#
# print(file)
# print(file.read())


# f = open('data.txt')
# print(f)
# print(f.readline())
# f.close()
# print(f)
# print(f.readline())


""" КОГДА ФАЙЛА НЕТ """
# try:
#     with open('data.txt') as file:
#         print(file.read())
# except IOError:
#     print('Error')


""" PRINT В ФАЙЛ """
# with open('data.txt', 'w') as file:
#     print('From print', file=file)


with open('data.txt', 'w') as file:
    strings = ['Anna', 'John']
    print('\n'.join(strings), file=file)
