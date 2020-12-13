""""""""""""""""""
"""  FUNCTOOLS """
""""""""""""""""""
from functools import reduce, partial


############
#  REDUCE  #
############
def my_prod(total, amount):
    return total * amount


arr = [30, 53, 42, 35]
# [30, 53, 42, 35] -> ((((30) + 53) + 42) + 35)
total_prod = reduce(my_prod, arr)
print(total_prod)

total_prod = reduce(
    lambda total, amount: total * amount,
    arr
)
print(total_prod)


############
#  PARTIAL #
############
def pow(a, b):
    return a ** b


pow_2 = partial(pow, b=2)
pow_3 = partial(pow, b=3)
print(pow_2(3))
print(pow_3(3))


def division(a, b, c):
    return a / b + c


partial_obj = partial(division, c=3)
partial_obj_2 = partial(partial_obj, b=2)
print(partial_obj_2(10))
print(partial_obj_2(20))


""""""""""""""""""
"""  ITERTOOLS """
""""""""""""""""""
from itertools import count, cycle
from time import sleep


# c = 100
# while True:
#     c += 10
#     if c > 200:
#         break
#     print(c)

# бесконечная итерация
for i in count(100, 10):
    if i > 200:
        break
    print(i)


a = [2, 3, 4, 5]
for i in cycle(a):
    print(i)
    sleep(1)
