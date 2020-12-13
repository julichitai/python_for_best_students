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


def my_two_div(num1, num2):
    return num1 / num2, num2/ num1


print(my_two_div(2, 5))


def my_prod(num1, num2):
    if not num1:
        return
    return num1 * num2

# print(my_prod(None, 2))
