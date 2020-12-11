""""""""""""""
""" СТРОКА """
"неизменяемый"
""""""""""""""
empty_string = ''

""" КОНКАТЕНАЦИЯ """
first_name = 'Anna'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
full_name_format = f'{first_name} {last_name}'

print(full_name, full_name_format)
multiple = 'anna' * 7
print(multiple)
# конкатенация - когда не знаете, сколько значений будет всего, к примеру, считывание файлы, цикл
# а в других случаях, лучше использовать f-строки


""" ВЗЯТИЕ ЭЛЕМЕНТА ПО ИНДЕКСУ """
number = '1567s90213'
letter_index = 4
print(number[letter_index])


""" ИЗВЛЕЧЕНИЕ СРЕЗА """
""" [start:end:step] """
print(number[0:4], number[5:])


""" ШАГ """
numbers = '123456789'
odd_numbers = numbers[::2]
print(odd_numbers)

even_numbers = numbers[1::2]
print(even_numbers)


""" РЕВЕРС """
reversed_numbers = numbers[::-1]
print(reversed_numbers)


""""""""""""""""""""""""""
""" ФУНКЦИИ СО СТРОКАМИ"""
""""""""""""""""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html """
print('Capitalize', full_name.capitalize())
print('Swapcase', full_name.swapcase())
print('Lower', full_name.lower())
print('Upper', full_name.upper())
print('Replace A to I', full_name.replace('A', 'I'))

num = '1014'
print(num, 'is digit?', num.isdigit())


""" РАЗБИЕНИЕ СТРОКИ НА ЭЛЕМЕНТЫ СПИСКА """
obj = '1234-5678'
split_obj = obj.split('-')
print(split_obj)

file = 'a lot of text\nmore text\neven more text'
print(file)
print(file.split('\n'))


""" ОБРАТНАЯ ОПЕРАЦИЯ """
print('-'.join(split_obj))
