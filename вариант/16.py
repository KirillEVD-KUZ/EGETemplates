def f(x):
    if x<222:
        return 111
    if x>=222:
        return 2*(x+4)+f(x-3)
print(f(55555))