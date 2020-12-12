###########
# ФУНКЦИИ #
###########

username = 'Anna'
print(f'Hello, {username}')  # моментальное выполнение

username = 'John'
print(f'Hello, {username}')
# дублирование кода - плохо


###################
# ПРОСТЫЕ ФУНКЦИИ #
###################
# переиспользование кода - хорошо
def hello_user(name):
    print(f'Hello, {name}')


hello_user('Anna')
hello_user('John')


####################
# ФУНКЦИИ С RETURN #
####################
def my_prod(num1, num2):
    res = num1 * num2
    return res


print(my_prod(2, 5))


def my_prod(num1, num2):
    if not num1:
        return
    return num1 * num2

# print(my_prod(None, 2))


#############################
# ОБЛАСТЬ ВИДИМОСТИ ФУНКЦИИ #
#############################
def my_prod_input():
    num1 = int(input('Enter num1 >>> '))
    num2 = int(input('Enter num2 >>> '))
    return num1 * num2


# print(my_prod_input(), num1)
# num1 - локальная переменная функции

# num1, num2 = 3, 2


def my_prod_input_global():
    global num1, num2
    return num1 * num2


# print(my_prod_input_global(), num1)


def my_prod_input_nonlocal():
    num1 = int(input('Enter num1 >>> '))
    num2 = int(input('Enter num2 >>> '))

    def int_func():
        nonlocal num1, num2
        return num1 * num2
    return int_func()


print(my_prod_input_nonlocal())


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
