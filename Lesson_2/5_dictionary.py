""""""""""""""
""" СЛОВАРЬ"""
" изменяемый "
""""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html """
empty_dict = {}
old_dict = dict(name='Anna', age=18)
new_dict = {'name': 'Anna', 'age': 18}  # ключ в кавычках обязательно
print(new_dict)

""" ПОЛУЧЕНИЕ ВСЕХ КЛЮЧЕЙ И ЗНАЧЕНИЙ """
# print(new_dict.keys())
# print(new_dict.values())
#
# print(new_dict.items())

""" ПОЛУЧЕНИЕ КОНКРЕТНОЕ ЗНАЧЕНИЕ """
# print(new_dict['name'])
# print(new_dict.get('age'))

# print(new_dict['surname'])
# print(new_dict.get('surname'))
# if new_dict.get('surname') == None:
#     print('no surname')


""" ДОБАВЛЕНИЕ """
new_dict.update({'name': 'Inna'})

new_dict.update({'surname': 'Smith'})


""" УДАЛЕНИЕ """
# print('popped', new_dict.pop('name'))

# print('popped', new_dict.popitem())
# print(new_dict)


""" ПРИМЕНЕНИЕ """
number = input('Enter string number: ')
if number == 'one':
    print(1)
elif number == 'two':
    print(2)
elif number == 'three':
    print(3)

numbers_dict = {'one': 1, 'two': 2, 'three': 3}
print(numbers_dict[number])
