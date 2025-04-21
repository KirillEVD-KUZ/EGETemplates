for n in range(4,10000):
    a="3"+"1"*n
    while "31" in a or "211" in a or "1111" in a:
        if "31" in a :
            a=a.replace("31","1",1)
        if "211" in a:
            a=a.replace("211","13",1)
        if "1111" in a:
            a=a.replace("1111","2",1)
    if (a.count("1")+(a.count('2')*2)+(a.count("3")*3))==15:
        print(n)

#50