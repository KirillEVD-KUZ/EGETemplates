"""
#16833
p=list(range(25,73))
q=list(range(75,118))
mx=0
for d in range(200):
    for b in range(200):
        a=range(d,b)
        if all(((x in a) and (not(x in q))) <= ((x in p) or (x in q)) for x in range(200)):
            mx=max(mx,b-d)
print(mx)"""

"""#17871
p=list(range(14,40))
q=list(range(21,63))
mn=100
for start in range(100):
    for end in range(100):
        a=range(start,end)
        if all((x in p) <=(((x in q) and (not(x in a))) <=(not(x in p))) for x in range(100)):
            mn=min(mn,end-start)
print(mn)
#19"""