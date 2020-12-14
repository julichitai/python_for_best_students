""""""""""""""""""""
""" МОДИФИКАТОРЫ """
""""""""""""""""""""

""" r - Открыть файл на чтение (режим по умолчанию) """
# with open('data.txt', 'r') as f:
#     print(f.read())
#     # print(f.write('hello')) нельзя


""" w - Открыть на запись. При этом удалить содержимое файла. Если файл не существует, создать новый. """
# with open('data.txt', 'w') as f:
#     # print(f.read()) нельзя
#     print(f.write('hello'))


""" x - Открыть файл на запись, если он не существует. Если файл существует, он не будет создан. """
# with open('data.txt', 'x') as f:
#     # print(f.read()) нельзя
#     print(f.write('hello'))

# with open('new.txt', 'x') as f:
#     print(f.write('hello'))


""" a - Открыть файл на дозапись. Добавить информацию в конец файла. """
# with open('data.txt', 'a') as f:
#     print(f.write('hello!!!'))


""" b - Открыть файл в двоичном формате. """
# with open('data.txt', 'rb') as f:
#     print(f.read())


""" t - Открыть файл в текстовом формате (режим по умолчанию) """
# with open('data.txt', 'at') as f:
#     print(f.write('\nupdate'))


""" + - Открыть файл на чтение и запись """
with open('data.txt', 'r+') as f:
    print(f.read())
    print(f.write('hello'))
