import random
for n in range(6,101):
    a1="0"*19 + "1"*n + "2"*19
    for i in range(100):
        a=list(a1)
        random.shuffle(a)
        a="".join(a)
        