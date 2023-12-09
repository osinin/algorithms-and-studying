"""
Напишите функцию RLE кодирование для входной строки. Название функции должно быть rle_encode.
Вывод функции значение строчного типа (String).

Пример работы функции:
rle_encode('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW') -> '9W3B24W1B14W'
rle_encode('ABCABCABCDDDFFFFFF') -> '1A1B1C1A1B1C1A1B1C3D6F'
"""


def rle_encode(s):
    encoded = ''
    counter = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
        else:
            encoded = encoded + str(counter) + s[i]
            counter = 1
    encoded = encoded + str(counter) + s[-1]
    return encoded


a = rle_encode('ABCABCABCDDDFFFFFF')
print(a)



