import random

def askForWords(words):
    while len(words) != 0:
        wordEng = random.choice(list(words.keys()))
        userTranslate = input(f'Как переводится слово {wordEng}?: ')
        if userTranslate == words.get(wordEng):
            print(f'Верно! слово {wordEng} переводиться как: {words.get(wordEng)} \n')
            words.pop(wordEng)
        else:
            print(f'Не Верно! слово {wordEng} переводиться как: {words.get(wordEng)} \n')


easyWords = {
    'food': 'еда',
    'bike': 'велосипед',
    'apple': 'яблоко',
    'do': 'делать',
    'table': 'стол'
}
askForWords(easyWords)
print('Поздравляю, вы запомнили все слова! Переходим на новый уровень!')

hardWords = {
    'chainsaw': 'бензопила',
    'squirrel': 'белка',
    'castle': 'замок',
    'homeland': 'родина',
    'sewerage': 'канализация',
    'bottom': 'дно'
}

askForWords(hardWords)
print('Поздравляю, вы запомнили все слова! Переходим на новый уровень!')