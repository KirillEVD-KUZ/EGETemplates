def f(n):
    if n < 10:
        return n
    if n % 2 == 0:
        return f(n % 10) + f(n // 10)
    else:
        return f(10 ** n) + f(n % 10) - 2
k=0
for i in range(0,10**11):
    if f(i) == 0:
        k+=1
print(k)
