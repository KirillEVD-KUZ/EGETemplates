"""print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(x or y))and (not (w)) or (not(z or w)) and y):
                    print(x,y,z,w)"""


print("2 -", "wyzx")

"""mn=1000
for n in range(1,100):
    b=bin(n)[2:]
    if n%3==0:
        b=b+b[-2:]
    else:
        ost=bin((n%3)*3)[2:]
        b=b+ost
    res=int(b,2)
    if res>=195 and res<mn:
        mn=res
print(mn)"""
print("5 -", "199")

"""from turtle import *
tracer(0)
koef=10

for i in range(2):
    forward(23*koef)
    left(90)
    backward(27*koef)
    left(90)
up()
backward(5*koef)
right(90)
forward(11*koef)
left(90)
down()

for i in range(2):
    forward(26*koef)
    right(90)
    forward(32*koef)
    right(90)
up()
for x in range(-koef*5, koef*5):
    for y in range(-koef *5,koef*5):
        goto(x*koef,y*koef)
        dot(3)
exitonclick()"""
print("6 -", 22*17)

"""import itertools
k=0
for i in itertools.product("0123456", repeat=7):
    a="".join(i)
    if (a.count("0")+a.count("2")+a.count("4")+a.count("6"))==2:
        k+=1
print(k)"""
print("8 -", "81648")

"""mx=0
for n in range(4,10000):
    a="8"+"4"*n
    while "11" in a or "444" in a or "8888" in a:
        if "11" in a:
            a=a.replace("11","4")
        if "444" in a:
            a=a.replace("444","88")
        if "8888" in a:
            a=a.replace("8888", "1")
    if ((a.count("8")*8)+(a.count("4")*4)+(a.count("1")))>mx:
        mx=((a.count("8")*8)+(a.count("4")*4)+(a.count("1")))
print(mx)"""
print("12 -", "106")

"""from ipaddress import*
k=0
for i in ip_network("112.208.0.0/255.255.128.0",0):
    b=bin(int(i))
    if b.count("1")%11==0:
        k+=1
print(k)"""
print("13 -",3003)


"""a=(4*(3125**2019))+(3*(624**2020))-(2*(125**2021)) +(25**2022) -(4*(5**2023)) -2024
sp=[]
k=0
while a>0:
    sp.append(a%25)
    a//=25
for i in range(len(sp)):
    if sp[i]>10:
        k+=1
print(k)"""
print("14 -", "2256")

"""for a in range(1,1000):
    f=True
    for x in range(1,1000):
        if not((not(x%a==0)) <= ((x%28==0)<=(not(x%49==0)))):
            f=False
    if f:
        print(a)"""
print("15 -", "196")

"""from functools import*
@lru_cache(None)
def f(n):
    if n<=3:
        return 2025
    if n>3:
        return 3*(n-1)*f(n-2)
for n in range(1,2020):
    f(n)
print(f(2027)//f(2023))"""
print("16 -", "36905616")

"""a=list(map(int,open("17_16383.txt").readlines()))
mx=-100000
sp=[]
for i in range(len(a)):
    if a[i]>mx and len(str(abs(a[i])))==5 and abs(a[i])%100==21:
        mx=a[i]
mx=mx**2
for i in range(len(a)-1):
    if ((abs(a[i])%100==21 and len(str(abs(a[i])))==5)+(abs(a[i+1])%100==21 and len(str(abs(a[i+1])))==5))==1:
        if ((a[i]**2)+(a[i+1]**2))>=mx:
            sp.append(((a[i]**2)+(a[i+1]**2)))
print(len(sp), max(sp))"""
print("17 -", "74 17554376405")

"""def game(heap,moves,to):
    if heap>=435:
        return moves%2==to%2
    if moves==to:
        return 0
    h=[game(heap+5,moves+1,to),
       game(heap*3,moves+1,to)]
    return any(h)

def game1(heap,moves,to):
    if heap>=435:
        return moves%2==to%2
    if moves==to:
        return 0
    h=[game1(heap+5,moves+1,to),
       game1(heap*3,moves+1,to)]
    return any(h) if (moves+1)%2==to%2 else all(h)
print("19 -", min(s for s in range(1,435) if not game(s,0,1) and game(s,0,2)))
print("20 -", [s for s in range(1,435) if not game1(s,0,1) and game1(s,0,3)])
print("21 -", [s for s in range(1,435) if not game1(s,0,2) and game1(s,0,4)])
"""
print("19 - 49")
print("20 - 47 48")
print("21 - 130")

"""def f(x,y):
    if x==y:
        return 1
    if x>y or x==16:
        return 0
    else:
        return f(x+1,y)+f(x+2,y)+f(x*3,y)
print(f(2,9)*f(9,18))"""
print("23 -",325)

"""from fnmatch import fnmatch

for i in range(0, 10 ** 10, 98591):
   if fnmatch(str(i), "5?2*3?3?"):
       print(i, i//98591)"""
print()
print("25 -")
print("52253230 530")
print("5024493133 50963")
print("5125253135 51985")
print("5226013137 53007")
print("5326773139 54029")
print("5524053730 56030")
print("5624813732 57052")
print("5725573734 58074")
print("5826333736 59096")
print("5927093738 60118")
print()
