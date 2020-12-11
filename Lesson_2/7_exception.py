""""""""""""""""""
""" ИСКЛЮЧЕНИЯ """
""""""""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html """
new_dict = {'name': 'Anna'}

try:
    print(new_dict['age'])
except KeyError as error:
    print('error', error)
    print('invalid key')


""" ZeroDivisionError """
try:
    print(1 / 0)
except ZeroDivisionError as error:
    print('error', error)
    print('zero division')


""" KeyboardInterrupt """
# try:
#     while True:
#         pass
# except KeyboardInterrupt as error:
#     print('error', error)
#     print('enough')


""" Exception """
try:
    1 / 0
except Exception as error:
    print('error', error)
