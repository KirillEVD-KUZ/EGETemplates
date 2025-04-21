k=0
from itertools import*
for i in product("01234567", repeat=12):
    a="".join(i)
    if ((a.count("1")+a.count("3")+a.count("5")+a.count("7"))==3) and ("11" not in a) and ("13" not in a)and ("15" not in a)and ("17" not in a)and ("31" not in a)and ("31" not in a)and ("35" not in a)and ("37" not in a) and ("51" not in a)and ("53" not in a)and ("55" not in a)and ("57" not in a) and ("71" not in a)and ("73" not in a)and ("75" not in a)and ("77" not in a):
        k+=1
print(k)