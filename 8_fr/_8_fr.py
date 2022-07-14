
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
    for i in range(8):
        for x, y in e:
            if x == i or abs(y - k) == abs(x - i):
                break
        else:
            new_e = list(e)
            new_e.append((i, k))
            f(k + 1, new_e)

def main():
    f(0, [])
    print("solutions:", sols)

main()