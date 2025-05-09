"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def occupation_by_age(age):
    """

    :param age:
    :return:
    age < 7 - детcкий сад
    7<= age <= 17 - школа
    18 <= age <= 23 - вуз
    age >23 - работать
    """

    if age < 7:
        return "детский сад"
    elif 7 <= age <= 17:
        return "школа"
    elif 18 <= age <= 23:
        return "вуз"
    else:
        return "работа"


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #pass
    age = int(input("input your age: "))
    occ = occupation_by_age(age)
    print(occ)


if __name__ == "__main__":
    main()
