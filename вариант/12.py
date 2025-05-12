a="4"*222
k=0
while "4444" in a or "222" in a:
    if "4444" in a:
        a=a.replace("4444","2",1)
        k+=1
    else:
        a=a.replace("222","44",1)
        k+=1
print(k)