"""
Часть No1
Дан массив связей пользователей. Вам необходимо реализовать функцию,
которая принимает на вход три аргумента: информация о связях, как кортеж (tuple)
кортежей, первое имя (str), второе имя (str). Функция должна возвращать True, если
связь между любыми двумя заданными пользователями существует, например, если у
двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д., иначе
False.
"""


def check_relation(net: tuple, first: str, second: str) -> bool:
    """
    1. Создаем множество и добавляем в него первое имя (first) - в дальнейшем здесь будет строиться цепочка связей
    2. Создаем бесконечный цикл, внутри которого будем проходить по кортежу (net) циклом for
    3. Внутри цикла for проверям входит ли хотя бы одно имя из пары в наше множество. Если да - добавляем второе имя
       из пары в наше множество
    4. Делаем проверку. Если второе имя (second) находится в нашем множестве - циклы прерываются, функция возвращает True
    5. Если, после того как мы прошлись циклом по всему кортежу (net), со вторым именем (second) совпадений не было, мы
       делаем проверку, добавились ли вообще новые имена в наше множество с цепочкой связей? Если новых имен не добавилось -
       значит связей между именами нет, циклы прерываются, функция возвращает False. Если же новое имя было добавлено в
       множество - переходим на новую итерация цикла while
    """
    check = {first, }
    while True:
        num = len(check)
        for x, y in net:
            if x in check or y in check:
                check.update([x, y])
            if second in check:
                return True
        if len(check) == num:
            return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
