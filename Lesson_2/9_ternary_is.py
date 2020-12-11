""""""""""""""""""""""""""
""" ТЕРНАРНЫЙ ОПЕРАТОР """
""""""""""""""""""""""""""
a = 10
b = 40
max_num = None

if a > b:
    max_num = a
else:
    max_num = b

print(max_num)

max_num = a if a > b else b
print(max_num)


""""""""""""""""""""
""" ОПЕРАТОР  IS """
""""""""""""""""""""
name = 'Anna'
print(name == 'Anna')
print(name is 'Anna')  # проверяет идентичность двух объектов в памяти

a = 1
print(a is 1)
print(1 + a == 2)
print([1, 2, 3] is [1, 2, 3])  # False
print([1, 2, 3] == [1, 2, 3])  # True

# примитивные объекты они записываются напрямую в память (int, str, etc)
# а листы - изменяемые типы, которые хранятся по ссылкам
# == - сраванивает значения, а is - адреса памяти

arr1 = [1, 2, 3]
arr2 = arr1
arr2[0] = 100
print(arr2, arr1)  # [100, 2, 3] [100, 2, 3]


arr1 = [1, 2, 3]
arr2 = arr1.copy()
arr2[0] = 100
print(arr2, arr1)
