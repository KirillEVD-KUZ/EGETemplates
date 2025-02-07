def f(x, y, u5=0, u3=0, p45=0):
    if x > y :
        return 0
    if x == y and u5 <= 4 and u3 >= 2 and p45 == 5 :
        return 1
    else:
        return f(x * 5, y, u5 + 1, u3, p45) + f(x * 3, y, u5, u3 + 1, p45) + f(x + 45, y, u5, u3, p45 + 1)

print(f(1, 2970))
