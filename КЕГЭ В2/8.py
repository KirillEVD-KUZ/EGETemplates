import itertools
k=0
n=0
a=itertools.product("ЕЛОПРСТ", repeat=5)
for sl in a:
    n+=1
    if a[:-1]!="Е" and a[:-1]!="О" and (sl.count("Л")+sl.count("П")+sl.count("Р")+sl.count("С")+sl.count("Т"))<=3: