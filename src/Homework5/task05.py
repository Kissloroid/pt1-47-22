"""
Модуль collections имеет defaultdict, который дает вам значение по умолчанию для попытки
получить значение ключа, которого нет в словаре, вместо того, чтобы вызвать ошибку. Почему бы
не сделать это для списка?
Ваша задача — создать класс (или функцию, возвращающую объект) с именем DefaultList. Класс
будет иметь два параметра: список и значение по умолчанию. Список, очевидно, будет списком,
соответствующим этому объекту. Значение по умолчанию будет возвращено каждый раз, когда индекс
списка вызывается в коде, который обычно вызывает ошибку
(т. е. i > len(list) - 1 или i < -len(list)).
Этот класс также должен поддерживать обычные функции списка: расширение, добавление, вставка,
удаление и извлечение (extend, append, insert, remove, and pop).
"""


class DefaultList(list):

    def __init__(self, list_val: list, default_item=None):
        self.list_val = list_val
        self.default_item = default_item
        super(DefaultList, self).__init__(self.list_val)

    def __getitem__(self, y):
        try:
            super(DefaultList, self).__getitem__(y)
        except IndexError:
            return self.default_item


