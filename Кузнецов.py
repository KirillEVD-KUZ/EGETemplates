
"""print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not(x<=y)) or (z==w) or z):
                    print(x,y,z,w)"""
print("№2 - zyxw")

"""mx=0
for x in range(1,100):
    tr=""
    x1=x
    while x1>0:
        tr+=str(x1%3)
        x1//=3
    tr=tr[::-1]
    if x%3==0:
        tr=tr+tr[-2:]
    else:
        ost=(x%3)*3
        tr1=""
        while ost>0:
            tr1+=str(ost%3)
            ost//=3
        tr1=tr1[::-1]
        tr=tr+tr1
    res=int(tr,3)
    if res<=150 and x>mx:
        mx=x
    print(mx)"""
print("№5 -",16)

"""from turtle import *
tracer(0)
koef=10
for i in range(2):
    forward(28*koef)
    right(90)
    forward(18*koef)
    right(90)
up()
forward(14*koef)
right(90)
forward(10*koef)
left(90)
down()
for i in range(2):
    forward(30*koef)
    right(90)
    forward(7*koef)
    right(90)
up()
for x in range(-koef*5,koef*5):
    for y in range(-koef*5,koef*5):
        goto(x*koef,y*koef)
        dot(3)
exitonclick()"""
print("№6 -",15*8)


"""import itertools
n=0
sp=[]
for i in itertools.product("АБДЕОП", repeat=6):
    a="".join(i)
    n+=1
    if n%2==0:
        if a[:1]=="О":
            if ((a.count("А")==1)+(a.count("Б")==1)+(a.count("Д")==1)+(a.count("Е")==1)+(a.count("О")==1)+(a.count("П")==1))==6:
                sp.append(n)
print(max(sp))"""
print("№8 -",38306 )

"""for n in range(4,10000):
    a="4"+"2"*n
    while "42" in a or "8222" in a or "2222" in a:
        if "42" in a:
            a=a.replace("42","2")
        if "8222" in a:
            a=a.replace("8222", "24")
        if "2222" in a:
            a=a.replace("2222","8")
    if  (a.count("2")*2+a.count("4")*4+a.count("8")*8)==110:
        print("№12 -",n)"""
print("№12 -",59)

"""import ipaddress
i=ip_network("11.92.135.56/255.224.0.0",0)
print(i)
for q in ip_network("11.64.0.0/255.224.0.0",0):
    print(q)
"""
print("№13 -",1195255254)

"""mx=0
mX=0
for x in range(1,3001):
    a=(4**210)-(4**110)-x
    ch=""
    while a>0:
        ch+=str(a%4)
        a//=4
    ch=ch[::-1]
    if mx<ch.count("0"):
        mx=ch.count("0")
        mX=x
print(mX)"""
print("№14 -",1024)

"""b=list(range(36,75))
c=list(range(60,110))
mn=100000000
for start in range(1,200):
    for end in range(1,200):
        a=range(start,end)
        if all((not(x in a)) <=((x in b) == (x in c)) for x in range(1,200)):
            mn=min(mn, end-start)
print(mn)"""
print("№15 -",74)

from functools import*
lru_cache(None)
def f(n):
    if n<20:
        return n
    if n>=20:
        return (n-6)*f(n-7)
for n in range(0,47873):
    f(n)
print((f(47872) - 290*f(47865))/f(47858))