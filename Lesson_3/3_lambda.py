#########
# RANGE #
#########
print(range(10))
print(list(range(10)))
print(tuple(range(1, 10, 2)))

for i in range(10):
    print(i)


#####################
# АНОНИМНЫЕ ФУНКЦИИ #
#####################
def div_num(val_1, val_2):
    return val_1 / val_2


print(div_num(10, 2))
func = lambda x, y: x / 2
print(func(10, 2))

# пользоваться, когда выполняется операция только один раз
# с какой-то итерацией

n_tuple = (('apple', 30, 1000), ('pear', 53, 10000), ('banana', 42, 1), ('orange', 35, 10))
print(sorted(n_tuple, key=lambda x: x[2], reverse=True))

