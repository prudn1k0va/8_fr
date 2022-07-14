
from random import randint

sols = 0

def f(k, e):
    global sols
    if k == 8:
        print(e)
        for x, _ in e:
            print(('-' * x) + '*' + ('-' * (7 - x)))
        sols += 1
        return
