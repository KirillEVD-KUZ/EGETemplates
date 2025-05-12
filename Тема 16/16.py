"""#19882
from functools import*
@lru_cache(None)

def f(n):
    if n<4:
        return 1
    if n>=4:
        return f(n-1)+n*2

for n in range(1,2025):
    f(n)

print(f(2025))"""

"""#19248
from functools import*
@lru_cache(None)

def f(n):
    if n<5:
        return n
    if n>=5:
        return 2*n*f(n-4)

for n in range(1,13766):
    f(n)
print((f(13766)-9*f(13762))//f(13758))"""

"""# СТ 01.04
from functools import *


@lru_cache(None)
def f(n):
    if n <= 5:
        return 1000
    if n > 5:
        return n + 3 + f(n - 2)


for n in range(1, 53079):
    f(n)
print(3*f(53079)-f(53077)-f(53075)-f(53073))"""

# 2247
"""import sys
sys.setrecursionlimit(100000)
k = 0


def f(n):
    if n <= 3:
        return n
    if n >= 3 and n % 2 == 0:
        return n - 2 + f(n - 2)
    if n >= 3 and n % 2 != 0:
        return f(n + 2) + n + 2

for n in range(100, 2000,2):
    if 10000 <= f(n) <= 100000:
        k += 1

print(k)"""
"""import sys
sys.setrecursionlimit(100000)
k = 0


def f(n):
    if n <= 3:
        return n
    if n >= 3 and n % 2 == 0:
        return n - 2 + f(n - 2)
    if n >= 3 and n % 2 != 0:
        return f(n + 2) + n + 2

for n in range(100, 2000,2):
    try:
        if 10000 <= f(n) <= 100000:
            k += 1
    except:
        pass
print(k)"""

"""#2248
def f(n):
    if n<=1:
        return n
    if n>1 and n%3==0:
        return n+f(n//3)
    if n>1and n%3!=0:
        return n+f(n+3)
for n in range(1,1000):
    try:
        if f(n)>100:
            print(n)
            break
    except:
        pass"""
