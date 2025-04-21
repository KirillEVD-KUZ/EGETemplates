"""#14660
p=list(range(16,85))
q=list(range(27,44))
a=list(range(1,200))
for x in range(1,200):
    if (((x in a )<=(x in p)) or ( x in q))==0:
        a.remove(x)
print(a)

#7846
p=list(range(13,20))
q=list(range(17,24))
a=list(range(1,200))
for x in range(1,200):
    if (not((x not in p) <=(x in q)))<=((x in a ) <=((not(x in q ))))
        a.remove(x)
print(a)
"""
b=list(range(25,41))
