#####################
# АНОНИМНЫЕ ФУНКЦИИ #
#####################
def div_num(val_1, val_2):
    return val_1 / val_2


print(div_num(10, 2))
func = lambda x, y: x / y
print(func(10, 2))


square_lambda = lambda x: x ** 2
print(square_lambda(4))


print(
    (lambda *args: args)
    (1, 2, 3, 4)
)

# пользоваться, когда выполняется операция только один раз
# либо с какой-то итерацией
# lambda - быстрее обычной функции

n_tuple = (('apple', 30, 1000), ('pear', 53, 10000), ('banana', 42, 1), ('orange', 35, 10))
print(sorted(n_tuple, key=lambda x: x[2], reverse=True))

array = [1, 2, 56, 34, 89, 12]
print(sorted(array, key=lambda x: x % 10))


def residual_by_2(x):
    return x % 10


print(sorted(array, key=residual_by_2))


#########
# RANGE #
#########
print(range(10))
print(list(range(10)))
print(tuple(range(1, 10, 2)))


counter = 0
while counter < 10:
    print(counter)
    counter += 1

for i in range(10):
    print(i)


