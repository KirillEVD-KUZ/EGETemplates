def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 4 < 2:
        return f(n // 4) + n % 4
    elif n % 4 >= 2:
        return f(n // 4) + n % 4 -1


n = 0
while True:
    if f(n) == 27 and f(n + 1) == 16:
        print(n)
        break
    n += 1