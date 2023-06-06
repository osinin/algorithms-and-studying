def find_duplicates(numbers: list):
    d = {}
    l = []
    for n in numbers:
        cnt = numbers.count(n)
        d[n] = cnt
    for (key, value) in d.items():
        if value > 1:
            l.append(str(key))
    return l


numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7]
duplicates = find_duplicates(numbers)
print(duplicates)
print(' '.join(sorted(duplicates)))