def f(n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return (n % 10) * f(n // 100)
    elif n > 0 and n % 2 == 0:
        return f(n // 100)

count= 0
for i in range (10**7 , 9 * (10 **7) + 1 ):
    if f(i) == 25:
        count += 1
print(count)