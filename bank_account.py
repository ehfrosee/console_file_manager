"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
account = 0
purchase_list = []
def income():
    """
    Функция пополнения счёта
    """
    global account
    sum = int(input("Введите сумму пополнения: "))
    account += sum

def buy():
    global account, purchase_list
    sum = int(input("Введите сумму покупки: "))
    if sum > account:
        print("На счёте не достаточно денег для покупки.")
        return
    else:
        purchise = input("Введите название покупки: ")
        account -= sum
        purchase_list.append([purchise, sum])
        return
def print_purchase_list():
    for purchise in purchase_list:
        print("Покупка: {}, сумма {}".format(purchise[0], purchise[1]))

def bank_account():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        match choice:
            case '1':
                income()
            case '2':
                buy()
            case '3':
                print_purchase_list()
            case '4':
                break
            case _:
                print('Неверный пункт меню')
