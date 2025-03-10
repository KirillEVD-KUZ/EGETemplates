for A in range(1,100):
    b=True
    for x in range(1,100):
        if not((int(x//2==0) <= (not(int(x//5==0)))) or x+A>=80):
            b=False
    if b:
        print(A)
        break