import itertools
sm=0
for i in itertools.product("347", repeat=30):
    a = "".join(i)
    a = ">" + a

    if a.count("3")==10 and a.count("4")==10 and "a".count("7")==10:
        print(a)
        while ">3" in a or ">5" in a or ">7" in a :
            if ">3" in a :
                a=a.replace(">3","55>",1)
            if ">5" in a:
                a=a.replace(">5","5>3",1)
            if ">7" in a:
                a=a.replace(">7","3>5",1)
        a=a[-1:]
        print(a)
