#############################
# ОБЛАСТЬ ВИДИМОСТИ ФУНКЦИИ #
#         ЛОКАЛЬНАЯ         #
#############################
def my_prod_input():
    num1 = int(input('Enter num1 >>> '))
    num2 = int(input('Enter num2 >>> '))
    return num1 * num2


# print(my_prod_input(), num1)
# num1 - локальная переменная функции

counter = 0


def increment(c):
    print(c)
    c += 1
    print(c)


increment(counter)
print(counter)


#############################
# ОБЛАСТЬ ВИДИМОСТИ ФУНКЦИИ #
#        ГЛОБАЛЬНАЯ         #
#############################
def increment():
    global counter
    print(counter)
    counter += 1
    print(counter)


increment()
print(counter)


#############################
# ОБЛАСТЬ ВИДИМОСТИ ФУНКЦИИ #
#        НЕЛОКАЛЬНАЯ        #
#############################
def increment_start():
    start = 0

    def inner_func():
        nonlocal start
        start += 1
        return start
    return inner_func()


print(increment_start())


####################
# ДОКУМЕНТИРОВАНИЕ #
####################
def my_prod_2(num1: int, num2: int) -> int:
    """
    Произведение двух чисел
    :param num1: первый аргумент. целое число
    :param num2: второй аргумент. целое число
    :return: сумма, целое число
    """
    # TODO переписать доку
    res = num1 * num2
    return res


#########################
# ОТЛИЧИЯ func и func() #
# #########################
# def return_hello():
#     return f'Hello'
#
#
# hello = return_hello
# print(hello, hello())
# hello = return_hello()
# print(hello)
#
#
# #######################
# # ПРОДВИНУТЫЕ ТЕХНИКИ #
# #######################
# # ЕСЛИ ЕСТЬ ОДИНАКОВЫЙ ФУНКЦИОНАЛ В ФУНКЦИЯХ
# def prod2(num):
#     return num * 2
#
#
# def prod3(num):
#     return num * 3
#
#
# func_mapper = {
#     2: prod2,
#     3: prod3
# }
#
# prod_num = int(input('Enter prod num >>> '))
# prod_func = func_mapper[prod_num]
# print(prod_func(9))
