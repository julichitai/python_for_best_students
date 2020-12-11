""""""""""""""""""
""" ЦИКЛЫ  FOR """
""""""""""""""""""
data = [30, 22, 41]

# index = 0
#
# while index < len(data):
#     print(data[index])
#     index += 1

""" ИТЕРАЦИЯ ПО СПИСКУ """
for d in data:
    print(d)

""" ИТЕРАЦИЯ ПО СТРОКЕ """
for char in 'hello':
    print(char)

""" ИТЕРАЦИЯ ПО СЛОВАРЮ """
n_dict = {'name': 'Anna', 'age': 18}

for key, value in n_dict.items():
    print(key, value)

for key in n_dict.keys():
    print('key', key)

for value in n_dict.values():
    print('value is', value)
