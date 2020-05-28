# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить
# отдельный
# модуль
# mastermind_engine, реализующий
# функциональность
# игры.
# # В этом модуле нужно реализовать функции:
# #   загадать_число()
# #   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# # Загаданное число хранить в глобальной переменной.
# # Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

# Импортировать загаданное число нам не надо
# Тк проверка идёт внутри модуля engine, с тем числом, которое мы передадим в check
# Значит никакой нужды нам видеть это число здесь - нет



# Общай структура должна быть такой:
# цикл
#     загадывание_числа_комьютером()
#     отгадывание_числа_пользователем  -- это лучше вынести в отдельную функцию
#     запрос_пользователю_о_повторной_игре

# функцию с отгадыванием создать нужно здесь
# она будет получать инпутом число пользователя, проверять его в цикле (что-то вроде цикла while в 4.03 и 4.02)
# когда число будет проверено - нужно добавить +1 к количеству попыток
# и проверить число на совпадение с загаданным.
# если быков == 4, то цикл этой функции прерывается, если не 4, то начинается заново
from mastermind_engine import make_number, check_number
from termcolor import cprint, colored


def user_number():
    while True:
        us_num = input(colored('Введите четырехзначное число c неповт1оряющимися цифрами: ', 'green'))
        if len(us_num) != 4 or not us_num.isdigit() or us_num[0] == '0':
            cprint('Вы ввели не корректное число', on_color='on_cyan')
            continue
        us_num = list(map(int, us_num))
        if len(set(us_num)) == 4:
            break
        else:
            cprint('Число состоит из повторяюшихся символов', color='yellow')
    return us_num


def replay_query():
    player_num = 0
    while True:
        player_num += 1
        result = check_number(us_nums=user_number())
        for name in result:
            print(name, result[name])
        if result['быки'] == 4:
            cprint('Игрок угадал число !!!', color='red')
            print('количество попыток:', player_num)
            return result


while True:
    print('Ход игрока')
    make_number()
    replay_query()
    player = input(colored('Хотите еще партию? ', 'blue'))
    if player == 'Да':
        continue
    else:
        break

#зачет!