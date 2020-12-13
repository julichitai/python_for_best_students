#####################
# АРГУМЕНТЫ ФУНКЦИИ #
#####################
def div9_2():
    return 9 / 2


def div_num(val_1, val_2):
    return val_1 / val_2


###########################
# ПОЗИЦИОННЫЕ/ИМЕНОВАННЫЕ #
###########################
print(div_num(10, 2))  # позиционные
print(div_num(val_1=10, val_2=2))  # именованные
print(div_num(val_2=10, val_1=2))  # именованные
# print(div_num(val_2=10, 2))

params = [10, 2]
print(div_num(*params))


# params = [10, 2, 6]
# print(div_num(*params))


###############################
# ОБЯЗАТЕЛЬНЫЕ/НЕОБЯЗАТЕЛЬНЫЕ #
###############################
def print_person_info(name, surname, age=None):
    res_str = f'{surname} {name}'
    if age:
        res_str = res_str + f', {age} y.o.'
    print(res_str)


print_person_info('Anna', 'Smith', 18)


##########################################
# ЕСЛИ НЕ ЗНАЕМ СКОЛЬКО БУДЕТ АГРУМЕНТОВ #
#             ПОЗИЦИОННЫЕ                #
##########################################
def print_vals(val_1, val_2, val_3):
    print(val_1)
    print(val_2)
    print(val_3)


print_vals(1, 2, 3)


def print_vals(*args):
    for el in args:
        print(el, end=' ')
    print()
    # print(val_1)
    # print(val_2)
    # print(val_3)
    # print(args)


print_vals(1, 2, 3, 66, 77, 100)


##########################################
#             ИМЕНОВАННЫЕ                #
##########################################
def print_vals(**kwargs):
    for el in kwargs:
        print(el, end=' ')
    print()
    if kwargs.get('val_4') is None:
        print('there is no val_4')


params = {'val_1': 1,
          'val_2': 2,
          'val_3': 3}

print_vals(**params)
