from sys import*
setrecursionlimit(10000)
def f(x,y):
    if x==y:
        return 1
    if x<y or x==16:
        return 0
    if x%3==0:
        return f(x-2,y) + f(x//3,y)
    else:
        return f(x-2,y) + f(x-4,y)
print(f(36,4))