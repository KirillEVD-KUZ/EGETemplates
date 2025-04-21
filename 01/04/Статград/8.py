"""#БЛРСУЬЭ
#0123456
b=7
#ЬУССЛ
#54313
#43210
res=(5*b**4)+(4*b**3)+(5*b**2)+(3*b**1)+(3*b**0)
print(res)"""
from itertools import*
n=1
for p in product("БЛРСУЬЭ",repeat=5):
    s = ''.join(p)
    if s.count("С")>=2 and s.count("Л")==1 and "ЭЭ" not in s:
        if n%2==0:
            print(n)
    n+=1
