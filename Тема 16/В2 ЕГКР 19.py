import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
@lru_cache(None)
def f(n):
    if n<20:
        return n
    if n>=20:
        return (n-6)*f(n-7)
for n in range(1,47873):
    f(n)
print(f(47872)-((290*f(47865))/f(47858)))