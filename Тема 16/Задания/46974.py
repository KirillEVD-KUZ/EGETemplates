def f(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return f(n - 1) + 1
    elif n % 2 == 0 and n > 0:
        return f(n // 2)


count = 0
for i in range(100):
    print(i , f(i), bin(i)[2:])
print (bin(1000000000)[2:])