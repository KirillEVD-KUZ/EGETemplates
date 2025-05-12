for x in "0123456789abcd":
    a=int("4b3"+x+"1",14)
    b=int("5"+x+"f83",16)
    if (a+b)%13==0:
        print(x,(a+b)//13)