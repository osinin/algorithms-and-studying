l = [1, 2, 3, 4, 5, 6]
print(sorted(l, reverse=True))
print(list(reversed(l)))
print(l[::-1])
print(l[::-3])

d = {'a': 5, 'b': 10}
for i in d.items():
    print(i[1])

print(d.keys())


def test_lambda(**kwargs):
    a = 1
    my_func = lambda t1, t2: t1 * (t2 + a)
    return my_func


res = test_lambda(t1=5, t2=1)
print(res)

my_func = lambda t1, t2: t1 * t2
print(my_func(1, 2) * 5)