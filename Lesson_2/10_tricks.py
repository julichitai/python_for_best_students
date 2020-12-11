""""""""""""""""""""""""""""""
""" ПОЛЕЗНЫЕ ТРЮКИ  ПИТОНА """
""""""""""""""""""""""""""""""

""" ОБЪЕДИНЕНИЕ СПИСКОВ БЕЗ ЦИКЛА """
nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 6]
]
joined = sum(nums, [])
print(joined)


""" УДАЛЕНИЕ ДУБЛИКАТОВ В СПИСКЕ """
non_unique = [1, 2, 3, 4, 4, 4]
unique = list(set(non_unique))
print(unique)


""" ОБМЕН ЗНАЧЕНИЯМИ ЧЕРЕЗ КОРТЕЖИ """
a = 10
b = 23

a, b = b, a
print(a, b)


""" ПОИСК САМЫХ ЧАСТО ВСТРЕЧАЮЩИХСЯ ЭЛЕМЕНТОВ СПИСКА """
nums = [1, 2, 3, 4, 4]
print(
    max(set(nums), key=nums.count)
)


""" РАСПАКОВКА ПОСЛЕДОВАТЕЛЬНОСТЕЙ ПРИ НЕИЗВЕСТНОМ КОЛИЧЕСТВЕ ЭЛЕМЕНТОВ """
print(nums)
print(nums[0], nums[1])
print(*nums)


""" ВЫВОД С ПОМОЩЬЮ ФУНКЦИИ PRINT() БЕЗ ПЕРЕВОДА СТРОКИ """
print(*nums, sep='-', end='\n\n')


""" СОРТИРОВКА СЛОВАРЯ ПО ЗНАЧЕНИЯМ """
n_dict = {'apple': 30, 'pear': 53, 'banana': 42, 'orange': 35}
print(sorted(n_dict, key=n_dict.get))


""" НУМЕРОВАННЫЕ СПИСКИ """
for i, value in enumerate([12, 34, 'one', 'two'], start=1):
    print(i, value)