P=list(range(117,158))
Q=list(range(130,180))
mn=200
for a1 in range(1,200):
    for a2 in range(1,200):
            a=range(a1,a2)i
            if all(not(not ((x in P) <= ((not(x in a) and (x in Q)) <= (not(x in P)) )))for x in range(200)):
                mn=min(mn,a2-a1)
print(mn)

