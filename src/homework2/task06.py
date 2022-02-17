"""
Напишите программу, запрашивающую у пользователя целые числа,
пока он не оставит строку ввода пустой. После окончания ввода
на экран должны быть выведены сначала все отрицательные числа,
которые были введены, затем нулевые и только после этого положительные.
Внутри каждой группы числа должны отображаться в той последовательности,
в которой были введены пользователем.
Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2,
вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое значение
должно отображаться на новой строке.
"""


numbers = input('Введите число (пробел для окончания): ')
neg, zer, pos = [], [], []

while numbers != " ":
    if int(numbers) < 0:
        neg.append(numbers)
        numbers = input('Введите следующее число: ')
    elif int(numbers) == 0:
        zer.append(numbers)
        numbers = input('Введите следующее число: ')
    elif int(numbers) > 0:
        pos.append(numbers)
        numbers = input('Введите следующее число: ')
res_list = neg + zer + pos

for elem in res_list:
    print(elem, end='\n')