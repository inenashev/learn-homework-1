"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def is_string(a_str):
    return isinstance(a_str, str)


def string_comparison(str_a, str_b):
    len_a = 0
    len_b = 0
    if not (is_string(str_a) and is_string(str_b)):
        return 0
    else:
        len_a, len_b = len(str_a), len(str_b)

    if str_a == str_b:
        return 1
    elif str_b == "learn":
        return 3
    elif len_a > len_b:
        return 2
    else:
        return 42



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = {
        "a: not str, b: not str": (0, 42),
        "a: not str, b: str": (9, "some string"),
        "a: str, b: str": ("some string", "some string"),
        "a: str, b: learn": ("some string", "learn"),
        "a: learn, b: str": ("learn", "some string"),
        "a: abc, b: abcd": ("abc", "abcd"),
        "a: abcd, b: abc": ("abcd","abc")
    }

    for k, v in data.items():
        print(f'{k} : {string_comparison(v[0],v[1])}')


if __name__ == "__main__":
    main()
