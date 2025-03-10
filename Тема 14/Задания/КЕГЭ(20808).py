a=7**710+7**100
mx=0
mx1=0
for x in range(1,2031):
    a=a-x
    a1=a
    sm=""
    while a1>0:
        sm+=str(a1%7)
        a1//=7
    nl=sm.count("0")
    if nl==615:
        if x>mx1:
            mx1=x
print(mx1)

