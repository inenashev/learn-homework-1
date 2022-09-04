"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def sum_arr(arr):
    return sum(arr)


def mean_arr(arr):
    return sum(arr) / len(arr)


def sum_by_product(all_data):
    print("-----Суммарные продажи по товарам------")
    for d in all_data:
        print(f"Продукт: {d['product']}: {sum_arr(d['items_sold'])}")
        print()


def mean_by_product(all_data):
    print("-----Средние продажи по товарам------")
    for d in all_data:
        print(f"Продукт: {d['product']}: {mean_arr(d['items_sold'])}")
    print()




def sum_all(all_data):
    res = 0
    for d in all_data:
        res = + sum_arr(d['items_sold'])
    return res



def print_sum_all(all_data):
    print("-----Суммарные продажи по товарам------")
    print(f"Всего продано: {sum_all(all_data)}")
    print()


def mean_all(all_data):
    prod_cnt = len(all_data) #так делать плохо, но раз у нас данные простые и хорошие то ок
    return sum_all(all_data)/prod_cnt

def print_mean_all(all_data):
    print("-----Суммарные продажи по товарам------")
    print(f"Всего продано: {mean_all(all_data)}")
    print()


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    sum_by_product(data)
    mean_by_product(data)
    print_sum_all(data)
    print_mean_all(data)

if __name__ == "__main__":
    main()
