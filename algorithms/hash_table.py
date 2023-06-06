class HashTable:

    def __init__(self):
        # Формируем пустой список из 10 значений
        # Наша хеш таблица будет небольшой
        self.table = [None] * 10

    def _hash_function(self, key):
        # Функция которая вернет нам индексчисленное значение
        # а затем остаток от деления на 10, тем самым мы получим
        # индекс елемента
        return hash(key) % 10

    def add(self, key, value):
        # Этот метод поможет нам добавить
        # элемент в хеш таблицу

        # Получим индекс элемента, ключа
        hash_index = self._hash_function(key)

        # Проверим есть ли в этом индексе что то еще
        # Если нет то вставим массив в котоырй вставим
        # пару (ключ, значение)
        if self.table[hash_index] is None:
            self.table[hash_index] = []
        self.table[hash_index].append((key, value))

    def get(self, key):
        # Получим индекс элемента, ключа
        hash_index = self._hash_function(key)

        # Получим занчение элемента по индексу,
        # посчитанному черех хеш функцию
        bucket = self.table[hash_index]

        # Если пусто вернем ошибку
        if bucket is None:
            raise KeyError(key)

        # Получим доступ до элемента
        for k, v in bucket:
            if key == k:
                return v

        raise KeyError(key)

    def delete(self, key):
        # Получим индекс элемента, ключа
        hash_index = self._hash_function(key)

        # Получим занчение элемента по индексу,
        # посчитанному черех хеш функцию
        bucket = self.table[hash_index]

        # Если пусто вернем ошибку
        if bucket is None:
            raise KeyError(key)

        self.table.pop(tab._hash_function(key))
        return self.table



tab = HashTable()
print(tab.table)
tab.add('Dima', 'DE')
print(tab.table)
print(tab._hash_function('Dima'))
print(tab.get('Dima'))
print(tab.delete('Dima'))

