def countdown(val):
    """
    recursive func: counter value - 1
    """

    print(val)
    if val <= 0:
        return
    else:
        countdown(val-1)


def fact(val):
    """
    factorial
    """
    if val == 1:
        return 1
    else:
        print(f"{val} * {val-1}")
        return val * fact(val-1)


#countdown(10)
f = fact(4)
print(f)