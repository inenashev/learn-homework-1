"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    while True:
        try:
            user_input = input("Как дела? ")
            if user_input == "Хорошо": # а может lower и хорошо?
                print("Так то лучше")
                break
            print("Соберись")
        except KeyboardInterrupt:
            print()
            print("Пока")
            break

if __name__ == "__main__":
    hello_user()
