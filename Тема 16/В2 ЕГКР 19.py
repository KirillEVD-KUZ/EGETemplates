from functools import *


@lru_cache(None)
def f(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * f(n - 7)


for n in range(1, 47873):
    f(n)
print((f(47872) - 290 * f(47865)) // f(47858))
###################################################
nums = [0] * 50000
for n in range(len(nums)):
    if n < 20:
        nums[n] = n
    if n >= 20:
        nums[n] = (n - 6) * nums[n - 7]
print((nums[47872] - 290 * nums[47865]) // nums[47858])
