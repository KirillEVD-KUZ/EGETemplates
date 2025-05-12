for x in range(1125001,10000000000):
    for i in range(1,x):
        if x %i==0:
            if i%10==7 and i!=x and i!=7:
                print(x,i)


