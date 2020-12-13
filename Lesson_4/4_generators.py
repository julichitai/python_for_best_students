""""""""""""""""""""""""""""""
"""  НАСТОЯЩИЙ  ГЕНЕРАТОР  """
"""          YIELD         """
""""""""""""""""""""""""""""""
# range - generator
print(range(0, 5))


def user_generator():
    for user in ['Anna', 'John', 'Kate']:
        yield user


print(user_generator, type(user_generator()))
print(user_generator())

for item in user_generator():
    print(item)


names_generator = user_generator()
print(next(names_generator))
print(next(names_generator))
print(next(names_generator))
# print(next(names_generator))


""" ПРИМЕР С ПУЛЬКАМИ """
# один раз отработал, больше не будет

def bad_pistol():
    return 1
    return 2
    return 3


print(bad_pistol())


def nice_pistol():
    print('started')
    yield 1
    yield 2
    yield 3


pistol = nice_pistol()
print(next(pistol))
print(next(pistol))
print(next(pistol))
# print(next(pistol))


def ideal_pistol(num_bullet):
    shoot = 0
    while shoot < num_bullet:
        shoot += 1
        yield shoot


pistol = ideal_pistol(3)
print(next(pistol))
print(next(pistol))
print(next(pistol))
# print(next(pistol))


for bullet in ideal_pistol(3):
    print(bullet)

bullets = [i for i in ideal_pistol(3)]
print(bullets)


""" ЗАЧЕМ ОНО ВСЁ """
from datetime import datetime as dt
import sys


def make_list_range(start, finish):
    array = []
    while start < finish:
        array.append(start)
        start += 1
    return array


def make_range(start, finish):
    while start < finish:
        yield start
        start += 1


start = dt.now()
# array = make_list_range(0, 50_000_000)
array = make_range(0, 50_000_000)
print(f'Size of object is {sys.getsizeof(array)}')
print(f'Elapsed time {dt.now() - start} seconds')

# List function
# Size of object is 859724472
# Elapsed time 17.093281030654907 seconds


array = make_range(0, 10)

print(5 in array)
print(list(array))
print(5 in array)
print(list(array))
