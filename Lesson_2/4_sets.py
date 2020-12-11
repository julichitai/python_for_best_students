""""""""""""""""""
"""  МНОЖЕСТВА """
""" изменяемый """
""""""""""""""""""

""" только уникальные значения 
https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html """
empty_set = set()
a_set = {1, 2, 3, 3, 3, 2, 2}
print(a_set)


""" ДОБАВЛЕНИЕ ОБЪЕКТОВ """
a_set.add(5)
a_set.update({10})


""" УДАЛЕНИЕ ОБЪЕКТОВ """
a_set.remove(1)

a_set.discard(1)

popped = a_set.pop()

a_set.clear()


""" ВЫЧИСЛЕНИЯ СО МНОЖЕСТВАМИ """
a_set = {1, 2, 3}
b_set = {6, 3}
# print(a_set.difference(b_set))
# print(a_set.intersection(b_set))
# print(a_set.union(b_set))


""""""""""""""""""
""" FROZEN SET """
""""""""""""""""""

fr_set = frozenset((1, 2, 3, 3))
# print(fr_set)
