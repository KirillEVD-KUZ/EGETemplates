# 17678 (12)
"""def f(x,y):
    return (x+y<=24) or (y<=x-2) or (y>=a)
for a in range(0,200):
    if all(f(x, y)==1 for x in range(1,200) for y in range(1,200)):
        print(a)"""

# 17556 (88)
"""def f(x):
    return (x%a==0) or ((70<=x<=90) <=(x%22!=0))

for a in range(1,200):
    if all(f(x)==1 for x in range(1,200)):
        print(a)"""

# 14655 ()
"""def f(x):
    return (x & a != 0) <= ((x & 168 == 0) <= (x & 69 != 0))

for a in range(400, 1, -1):
    if all(f(x) == 1 for x in range(1, 300)):
        print(a)
        break"""

# 13082(60)
"""def f(x,y):
    return (3*x + y >48) or (x>y) or (4*x +y <a)

for a in range(0, 100):
    if any(f(x,y) == 0 for x in range(0,100) for y in range(0,100)):
        print(a)"""

# 12924 (3) множества макс
"""p={2,4,6, 8,10,12,14,16,18,20}
q={3,6,9,12,15,18,21,24,27,30}
a=set(range(1,100))
for x in range(1,100):
    if (((x in a )<=(x in p)) and ((not(x in q)) <= (not(x in a)))) == 0:
        a.remove(x)
print(len(a))"""

# 743 (12)
"""p={1,3,5,7,9,11}
q={3,6,9,12}
a=set()
for x in range(1,100):
    if (((x in p) <= (not(x in q))) or (x in a))==0:
        a.add(x)
print(a)"""

# 17528
k=[]
for p in range(15, 41):
    for q in range(21, 64):
        f = True
        for x in range(1, 40):
            if not ((x in p) <= (((x in q) and (not (x in a))) <= (x in p))):
                f = False
            if f:
                k.append(x)
print(len(k))
