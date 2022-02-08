import random


def compareAnswers(userAnswer, answer):
    if userAnswer == answer:
        print('Все верно!')
    else:
        print(f'А вот и нет! Правильный ответ {answer}')

def generateRandomNumberArray(Lenght):
    arr = [random.randint(1, 100) for x in range(Lenght)]
    return arr

numbers = generateRandomNumberArray(5)
print(f'Запомните числа и их порядок: {numbers}')

userAnswer = int(input('Каким было первое число?: '))
compareAnswers(userAnswer, numbers[0])

userAnswer = int(input('А последнее число?: '))
compareAnswers(userAnswer, numbers[-1])

n = random.randint(1, len(numbers) - 1)
userAnswer = int(input(f'А как на счет числа под номером {n + 1} ?: '))
compareAnswers(userAnswer, numbers[n])
