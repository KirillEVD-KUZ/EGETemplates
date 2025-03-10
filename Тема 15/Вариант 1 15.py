for a in range(100):
    b=True
    for x in range(100):
        if not((x//2) <= (not(x//5)) or (x+a>=80)):
            b=False
    if b:
        print(a)
# 76

