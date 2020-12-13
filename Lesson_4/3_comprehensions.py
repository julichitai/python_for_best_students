""""""""""""""""""""""""""""""
""" НЕНАСТОЯЩИЙ  ГЕНЕРАТОР """
""""""""""""""""""""""""""""""
array = []
for i in range(10):
    array.append(i * 2)
print(array)

""" СПИСКИ (LIST COMPREHENSION)"""
print([i for i in range(10)])
print([i * 2 for i in range(10)])

""" СПИСКИ С УСЛОВИЯМИ"""
print([i for i in range(10) if i % 2 == 0])


""" ПРИМЕР """
pin_code = '129'
# pin_code = '1290'
# pin_code = '1291'

pin_codes = [f'{pin_code}{i}' for i in range(0, 10)]
print(pin_codes)

pin_code = '12'
pin_codes = [f'{pin_code}{i}' if i > 10 else f'{pin_code}0{i}' for i in range(0, 100)]
print(pin_codes)

""" СПИСКИ СО ВЛОЖЕННЫМИ ЦИКЛАМИ """
sum_i_j = []
for i in range(10):
    for j in range(5):
        sum_i_j.append(i + j)
print(sum_i_j)
print(len(sum_i_j))
print(10 * 5)

sum_i_j = [i + j for i in range(10) for j in range(5)]
print(sum_i_j)
print(len(sum_i_j))


""" СЛОВАРИ """
result_dict = {key: key * 2 for key in range(5)}
print(result_dict)


keys = ['name', 'age']
values = ['Anna', 18]

result_dict = {key: value for key, value in zip(keys, values)}
print(result_dict)


""" МНОЖЕСТВА """
result_set = {num for num in [1, 2, 3, 4, 2, 1, 2]}
print(result_set)