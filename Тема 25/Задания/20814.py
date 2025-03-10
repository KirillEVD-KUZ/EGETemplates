for i in range(500000,1000000):
    sm=0
    for y in range(2,i):
        if i%y==0:
            sm+=y
    if sm%10==9:
        print(i, sm)