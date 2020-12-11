""""""""""""""
""" КОРТЕЖ """
"неизменяемый"
""""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html """
empty_tuple = tuple()
a_tuple = (1, 2, 3, 3)
print(type(a_tuple))

print(a_tuple[0], a_tuple[::-1])

# a_tuple.append()

print(a_tuple.count(3))
print(a_tuple.index(1))

a_tuple = (2, 3, 3, 5)  # но кортеж то не изменился, это новый кортеж
