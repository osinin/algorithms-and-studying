"""
Напишите функцию под названием palindrome_check, которая проверит, что входная строка - это палиндром.
Выводом функции должно быть значение логического типа (True, False).

Примеры работы функции:

palindrome_check('abcba') -> True
palindrome_check('rttr') -> True
palindrome_check('dsfgads') -> False

"""


def palindrome_check(s):
    l = int(round(len(s)/2, 0))
    return True if s[:l] == s[-l:][::-1] else False


a = palindrome_check('abcba')
print(a)
