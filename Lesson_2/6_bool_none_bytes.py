""""""""""""""""""""
""" БУЛЕВЫЕ ТИПЫ """
""""""""""""""""""""
print(5 > 1)
print(bool(5), bool(0), bool('0'), bool('False'))
# привести к булевому типу можно всё, но нужно проверять
print(bool(-20))
print(bool(None))
print(bool(''), bool(' '))


""" NONE TYPE """
# login = None
# if login == None:
# 	print('Ошибка')


""""""""""""""
"""  ЧИСЛО """
""""""""""""""
print(int(17.5))


""" ПЕРЕВОД В ДРУГИЕ СИСТЕМЫ СЧИСЛЕНИЯ """
""" https://ege-study.ru/ege-informatika/sistemy-schisleniya-perevod-iz-odnoj-sistemy-v-druguyu/"""
print(int('1001', 2))
print(bin(9))  # 0b - специальные префикс системы, можно его игнорировать
print(oct(9))
print(hex(9))  # цвета в пальтре в виде шестнадцатеричных значений


""" ПОБИТОВЫЕ ОПЕРАЦИИ """
""" https://math.spbu.ru/user/nlebedin/bit_operat_2017.pdf - методичка
ПРИМЕНЕНИЕ:
- экономия памяти
- повышение производительности (битовые операции могут выполняться одновременно над всями разрядами)
- работа с регистрами аппаратуры
- работа с ip-адресами
"""
a = 6
b = 10
a & b
' 0b111'
'0b1110'
' 0b110'

print(a | b)
' 0b111'
'0b1110'
'0b1111'
print(a ^ b)

' 0b111'
'0b1110'
'0b1001'
print(1 << 0)
print(1 << 1)
print(1 << 2)
print(bin(1), bin(2), bin(4))
print(4 >> 2)


""""""""""""
""" БАЙТЫ"""
""""""""""""
""" https://pythonworld.ru/tipy-dannyx-v-python/bajty-bytes-i-bytearray.html """

# byte - неизменяемые
byte_string = b'Hello, world'
print(byte_string)

simple_string = 'Hello, world'
print(type(simple_string), type(byte_string))

print('encoded', 'привет'.encode('utf-8'))  # строка закодируется в байты через utf-8 (общепринятая кодировка)

# bytearray - изменяемые, итого bytes - аналог кортежа, bytearray - аналог списка
byte_array_string = bytearray(byte_string)
print(byte_array_string, type(byte_array_string))


name = 'Anna'
byte_name = name.encode(encoding='utf-8')
print(byte_name, type(byte_name))

name = 'Anna'
byte_array_name = bytearray(name.encode(encoding='utf-8'))

print('ord', ord('I'))  # порядок числа по таблице ASCII
print('chr', chr(73))  # взять символ из таблицы ASCII
byte_array_name[0] = 73
print(byte_array_name, type(byte_array_name))
