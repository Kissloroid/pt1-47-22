"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере 4,00 BYN плюс 0,25 BYN за каждые 100 м поездки.
Напишите функцию, принимающую в качестве единственного параметра расстояние
поездки в километрах и возвращающую итоговую сумму оплаты такси. В основной
программе должен демонстрироваться результат вызова функции.
"""


def taxi_price(km):
    min_ride = 400
    cost_100_metres = 25
    price = km * 10 * cost_100_metres + min_ride

    return f'Стоимость поездки составит {int(price // 100)} рублей {int(price % 100)} копеек'


input_data = float(input('Введите расстояние в километрах: '))

print(taxi_price(input_data))