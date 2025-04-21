for a in range(1,100):
    f=1
    for x in range(1,100):
        if not((x&57==0)or ((x&23==0)<=(not(x&a==0)))):
            f=0
    if f:
        print(a)