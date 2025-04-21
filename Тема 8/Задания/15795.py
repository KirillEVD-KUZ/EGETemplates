"""from itertools import product
count = 1
for p in product("АПРСУ", repeat = 4):
    if "А" not in p:
        break
    count +=1
print(count)
"""
from itertools import*
n=1
for p in product("БЛРСУЬЭ",repeat=5):
    a="".join(p)
    if p.count("C")>=2 and p.count("Л")==1 and "ЭЭ" not in p:
        if n%2==0:
            print(n)
    n+=1