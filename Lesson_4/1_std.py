""""""""""""""""""""""""""""""""""""
""" ИМПОРТ  СТАНДАРТНЫХ  МОДУЛЕЙ """
""""""""""""""""""""""""""""""""""""
import time


start = time.time()
print(f'Started at {start}')

for i in range(10):
    time.sleep(0.1)

print(f'Finished at {time.time()}')
print(f'Elapsed time {time.time() - start}')


""" ИМПОРТ ОПРЕДЕЛЕННЫХ ФУНКЦИЙ """
from time import time, sleep


start = time()
print(f'Started at {start}')

for i in range(10):
    sleep(0.1)

print(f'Finished at {time()}')
print(f'Elapsed time {time() - start}')


""" ПЕРЕИМЕНОВАНИЕ ЗАИМПОРТИРОВАННЫХ ФУНКЦИЙ """
from time import time as std_time, sleep as std_sleep


start = std_time()
print(f'Started at {start}')

for i in range(10):
    std_sleep(0.1)

print(f'Finished at {std_time()}')
print(f'Elapsed time {std_time() - start}')


""" ЕЩЕ МОДУЛИ """
from datetime import datetime as dt

start = dt.now()
print(f'Started at {start}')

for i in range(10):
    sleep(0.1)

print(f'Finished at {dt.now()}')
print(f'Elapsed time {dt.now() - start}')

import random
import math

random_num_1, random_num_2 = random.random(), random.random()
print(f'{random_num_1} ** {random_num_2} = {math.pow(random_num_1, random_num_2)}')

# random.seed(4)
num = random.randint(4, 30)  # целое в указанном диапазоне
print(f'Random num is {num}')
sqrt_num = math.sqrt(num)
print(f'Sqrt is {sqrt_num}')
print(f'Ceil is {math.ceil(sqrt_num)}')
print(f'Floor is {math.floor(sqrt_num)}')
print(f'Round is {round(sqrt_num)}')

print(random.randrange(5, 10, 2))  # целое в указанном интервале
print(random.choice(['a', 'b', 'c', 'd', 'e']))  # вернет одно значение из последовательности

a = [100, 23, 56, 12]
random.shuffle(a)  # перемешивание
print(a)
