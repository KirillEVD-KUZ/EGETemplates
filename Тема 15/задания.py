"""20584
def f(x):
    return ((405%x==0)<=(81%x==0))or (a-x>162)
for a in range(1,600):
    if all(f(x)==1 for x in range(1,600)):
        print(a)"""
"""b=list(range(170, 221))
k=0
def f(x):
    return (x%a==0) or ((x in b)<=(not(x%24)))
for a in range(1,1500):
 if all(f(x)== 1 for x in range(1,1500)):
     k+=1
print(k)"""
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
