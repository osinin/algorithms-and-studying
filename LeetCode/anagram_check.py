"""
 Задание 5
Теперь проверим, что две входные строки - это анаграммы. Напишите функцию под названием anagram_check,
которая будет принимать на вход две строки.
Аналогично прошлому заданию выводом функции должно являться значение логического типа (True, False).

Примеры:
anagram_check('золотарник', 'разнотолки') -> True
anagram_check('Лунь', 'нуль') -> True
anagram_check('Воз', 'зов') -> True
anagram_check('песнь', 'снедь') -> False
"""


def anagram_check(s, ss):
    return True if list(sorted(s.lower())) == list(sorted(ss.lower())) else False


a = anagram_check('золотарник', 'разнотолки')
print(a)