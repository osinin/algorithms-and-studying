a = [95, 78, 76, 38, 98]
N = len(a)

for i in range(N - 1):
    print(f'i: {i}')
    for j in range(N - i - 1):
        print(f'j: {j}')
        if a[j] > a[j + 1]:
            print(f'{a[j]} switched with {a[j+1]}')
            a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
    print('------------------------------')


print(a)