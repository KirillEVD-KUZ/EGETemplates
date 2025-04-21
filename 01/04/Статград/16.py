from functools import lru_cache
@lru_cache(maxsize=None)

def f(n):
    if n <= 5:
        return 1000
    return n + 3 + f(n - 2)


print((3 * f(53079)) - (f(53077) + f(53075) + f(53073)))
