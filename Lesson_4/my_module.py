def div_num(val_1, val_2):
    val_1 = int(val_1)
    val_2 = int(val_2)
    return val_1 / val_2


def hello(name):
    print(f'Hello, {name}!')


CONSTANT = 15

if __name__ == '__main__':
    print('Запуск из my_module', div_num(20, 1))
