for n in range(1,100):
    a=">"+"0"*17+"3"*n+"2"*17
    while ">3" in a or ">2" in a or ">0" in a:
            a=a.replace(">3","22>",1)
            a=a.replace(">2","2>",1)
            a=a.replace(">0", "3>",1)
    a=a[:-1]
    sm=0
    for i in range(len(a)):
        sm+=int(a[i])
    print(n,a,sm)