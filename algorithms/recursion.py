"""
recursive func: counter value - 1
"""


def countdown(val):
    print(val)
    if val <= 0:
        return
    else:
        countdown(val-1)


countdown(10)