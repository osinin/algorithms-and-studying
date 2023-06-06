inp = 'a b c d,b:1 c:2 d:3'
left, right = list(map(str, inp.split(',')))
left = list(map(str, left.split()))
right = dict(map(lambda x: x.split(':'), right.split()))

def join(left, right):
    d = {}
    for i in left:
        if i in right.keys():
            d[i] = str(right[i])
        else:
            d[i] = 'default'
    return d

res = join(left, right)
print(res)