# 0. Словарь хранить глобально, но передавать как параметр
# 1. Нужна функция, которая спрашивает у пользователя перевод
#    предложенного слова и сравнивает с сохраненным у себя
# 2. Нужна функция, которая умеет пополнять словарь.
#    Она спрашивает пользователя ввести слово и перевод.
#    И запоминает результат
# 3* Сделать игру - подсчитывать процент ошибок

import random

words = {
    'hello': 'привет',
    'bye': 'пока',
    'name': 'имя',
    'family': 'семья'
}

def question_user(): # ПЕРЕВОДЧИК СЛОВ, КОТОРЫЕ ХРАНЯТСЯ В СЛОВАРЕ
    print(*words, '- ваш словарь английскийх слов')
    question = input('Введите слово, которое желайте перевести на русский язык: ')
    question = question.lower()
    if question in words:
        print('Ваше слово переводится:', words[question].title())
    else:
        say = input('Я не знаю такого слова, хотите его добавить?(да/нет) ')
        if say == 'да':
            new_words()


def new_words(): # РАСШИРЕНИЕ СЛОВАРЯ
    flag = True
    while flag == True:
        key_new_w = input('Введите слово на английском языке: ')
        trans_new_w = input('Введите перевод слова на русском языке: ')
        words[key_new_w] = trans_new_w
        print(words)
        say = input('Хотите добавить еще слово?(да/нет) ')
        if say == 'да':
            continue
        else:
            flag = False


def transl_word(): # УГАДАЙКА ПЕРЕВОДА АНГЛИЙСКОГО СЛОВА (СЛУЧАЙНОГО)
    say = 'да'
    while say == 'да':
        rand = random.choice(list(words)) # ПОДСМОТРЕЛ В ИНТЕРНЕТЕ
        print('Введите перевод слова: ', rand.title())
        word = input('Перевод: ').lower()
        if words[rand] == word:
            print('Да, верно!')
        else:
            print('Неверно')
        rep = input('Хотите попробывать еще раз? ').lower()
        if rep != 'да':
            say = 'нет'


def main_func(): # ГЛАВНАЯ ФУНКЦИЯ
    flag = True
    while flag == True:
        print('Введите, выберете нужную цифру для действия')
        print('1 - Показать словарь')
        print('2 - Угадать перевод слова')
        print('3 - Добавить новое слово')
        print('4 - Переводчик')
        print('5 - Закончить работу')
        user = int(input('Введице цифру для действия: '))
        if user == 1:
            print(words)
            action_1 = input('Хотите дальше продолжить работу?(да/нет) ').lower()
            if action_1 == 'да':
                flag = True
            else:
                flag = False
        elif user == 2:
            transl_word()
            action_2 = input('Хотите дальше продолжить работу?(да/нет) ').lower()
            if action_2 == 'да':
                flag = True
            else:
                flag = False
        elif user == 3:
            new_words()
            action_3 = input('Хотите дальше продолжить работу?(да/нет) ').lower()
            if action_3 == 'да':
                flag = True
            else:
                flag = False
        elif user == 4:
            question_user()
            action_4 = input('Хотите дальше продолжить работу?(да/нет) ').lower()
            if action_4 == 'да':
                flag = True
            else:
                flag = False
        else:
            print('Good Bye, My Friend!')
            flag = False
main_func()

