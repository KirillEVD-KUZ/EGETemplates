def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 4 < 2:
        return f(n // 4) + n % 4
    if n % 4 >= 2:
       return f(n//4) + n %4 - 1
"""for i in range(10000000,10000000000):
    if f(i)==27 and f(i+1) ==16:"""
print(f())