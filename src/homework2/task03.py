"""
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного
кортежа возвращает 1.
"""

tup = '123',

for char in tup[0]:
    print(char)
print(f'Длина кортежа составляет {len(tup)} символ')