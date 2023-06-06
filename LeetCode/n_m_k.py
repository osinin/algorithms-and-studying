"""
найти 2 числа в сумме дающие k
"""

k = 9
numbers = [-1, 2, 3, 7, 10]


def sum_of_two(num: list, find: int):
    for n in numbers:
        x = k - n
        if x in numbers:
            nn = numbers.index(x)
            if numbers[nn] == n and numbers.count(numbers[nn]) == 1:
                continue
            else:
                return n, numbers[nn]
        else:
            continue


answer = sum_of_two(numbers, k)
print(answer)
