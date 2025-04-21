"""# 5
mx=0
for x in range(1,1000):
    x1 = x
    vs = ""
    while x1 > 0:
        vs += str(x1 % 8)
        x1 //= 8
    vs = vs[::-1]
    if x % 2 == 0:
        vs = vs.replace("1", "2")
        vs = vs.replace("3", "2")
        vs = vs.replace("5", "2")
        vs = vs.replace("7", "2")
    else:
        vs="3"+vs[1:-1]+"3"
    otv=int(vs,8)
    print(x,vs,otv)
    if otv<300 and otv>mx:
        mx=otv
print(mx)"""
#8
"""k=0
import itertools
for i in itertools.product("ГЕИНРСЯ",repeat=6):
    a="".join(i)
    k+=1
    if a=="ЯЯГИРЯ":
        print(k)"""

#12
"""mn=10000
for n in range(6,100):
    a=">"+"0"*19+"1"*n+"2"*19
    while ">1" in a or ">2" in a or ">0" in a:
        if ">1" in a:
            a=a.replace(">1","22>",1)
        if ">2" in a:
            a=a.replace(">2","2>",1)
        if ">0" in a:
            a=a.replace(">0","1>",1)
    sm=0
    a=a[:-1]
    for q in range(len(a)):
        sm+=int(a[q])
    for w in range(len(str(sm))):
        if str(sm)[-1]==str(sm)[-2]:
            print(n,sm)"""

#№13
"""from ipaddress import*
for m in range(33):
    net=ip_network(f"111.233.75.16/{m}",0)
    if net.network_address ==  ip_address("111.233.75.0"):
        print(net.num_addresses)"""
#№14
"""mx=0
mxX=0
for x in range(1,10000):
    a=(7**270)+(7**170)+(7**70)-x
    a1=a
    sm=""
    while a1>0:
        sm+=str(a1%7)
        a1//=7
    sm=sm[::-1].lstrip("0")
    if sm.count("0")>mx and mxX<x:
        mx=sm.count("0")
        mxX=x
        print(mxX,mx)

a=(7**270)+(7**170)+(7**70)-2401
sm=""
a1=a
while a1 > 0:
    sm += str(a1 % 7)
    a1 //= 7
sm=sm[::-1]
print(sm.count("0"))"""


