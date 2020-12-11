""""""""""""""
""" СПИСКИ """
" изменяемый "
""""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html """
empty_list = []
array = [4, 5, 6, 1, 2, 7]
print(array)

""" ДОБАВЛЕНИЕ ОБЪЕКТОВ """
array.append(6)

array.extend([12, 11])

array += [0, 0]

array.insert(1, 44)

""" УДАЛЕНИЕ ОБЪЕКТОВ """
array.remove(1)

popped = array.pop(1)

""" ДРУГИЕ МЕТОДЫ """
counter = array.count(6)

array.sort()

found = array.index(2)
# print('index is', found)

# found = array.index(200)


array.sort(reverse=True)


""" СРЕЗЫ """
print(array[0], array[:3], array[::-1], array[-2:])


""" ПОМЕНЯТЬ ОБЪЕКТЫ МЕСТАМИ """
# print(array)
array[0], array[2] = array[2], array[0]
# print(array)
