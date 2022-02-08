"""
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

max = a

if a < b:
    max = b

print('Максимальное число',  max)

i = 0
while i < 5:
    print('Privet')
    i+=1
for i in range(1000):
    print('Privet', i)
    i+=1

n = int(input('Введите число n: '))
sum = 0

for i in range(n):
    i += 1
    sum += i
    print(i, " - ", sum)
"""

import random

answer = random.randint(1, 100)
print('Правильный ответ ', answer)
user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя игрока № {i+1}: ')
    users.append(user_name)
print(users)

count = 0
tryCount = 7
isWinner = False
print('Комп загадал число от 1 до 100, попробуйте угадать \n')


while not isWinner:
    print('У Вас осталось ', tryCount - count, ' попыток')
    count += 1
    if count > tryCount:
        print('Вы проиграли....... :(')
        print('Правильный ответ ', answer)
        break
    else:
        for user in users:
            print('Ход игрока ', user)
            userAnswer = int(input('Введите Ваше число: '))
            if userAnswer == answer:
                isWinner = True
                print('Вы угадали')
                break
            elif answer < userAnswer:
                print('Ваше число больше загаданного\n')
            else:
                print('Ваше число меньше загаданного\n')

print('Победил игрок ', user)