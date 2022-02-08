import math

# a = 'asdfdasfadsf'
# b = 'Всем'
#
# print('Привет,', a)
# print('Привет,', b)

# name = input('Введите ваше Имя: ')
# print('Привет', name)
# print('<----END---->')


# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))
# c = a*b
# print('Произведение чисел А*B= ', c)
# c = a+b
# print('Сумма чисел А+B= ', c)

# Курс ВАЛЮТ
curUsd = 76.05
curEuro = 81.12
curBit = 3153080

rubles = int(input('Веедите сумму в рублях: '))

print('Вы получите USD', round(rubles / curUsd, 2))
print('Вы получите USD', round(rubles / curEuro, 2))
print('Вы получите USD', round(rubles / curBit, 9))

a = int(input('Введите длину основания A: '))
b = int(input('Введите длину основания B: '))
h = int(input('Введите высоту H: '))
s = ((a+b)/2)*h
print('Площадь трапеции равна ', s)
