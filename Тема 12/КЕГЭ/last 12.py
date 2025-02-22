import random
for n in range(6,101):
    a=list(">" + "0" * 19 + "1" * n  + "2" * 19)
    random.shuffle(a)
    a="".join(a)
    if ">1" in a or ">2" in a or ">0" in a :
        if ">1" in a :
            a=a.replace(">1", "22>",1)
        if ">2" in a :
            a=a.replace(">2", "2>",1 )
        if ">0" in a:
            a=a.replace(">0", "1>", 1)
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    if sum[-1] == sum[-2] :
        print(n)
        break