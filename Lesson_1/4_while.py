""""""""""""""""""
""" ЦИКЛ WHILE """
""""""""""""""""""
# counter = 0
# while counter < 10:
#     print(counter)
#     counter = counter + 1
#     # counter += 1
# print('Цикл закончен')


""" BREAK """
# counter = 0
# while True:
#     if counter >= 10:
#         break
#     print(counter)
#     counter += 1
# print('Цикл закончен')


""" CONTINUE """
counter = 0
while True:
    if counter >= 10:
        break
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)
print('Цикл закончен')
