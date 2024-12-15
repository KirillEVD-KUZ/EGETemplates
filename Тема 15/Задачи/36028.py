p= range(17, 54)
q= range(37,83)
min_l=100
for begin in range(100):
    for end in range (begin, 100):
        a=range(begin,end)
        if all((x in p) <= (((x in q) and (not( x in A)) <= (not( x in p))))for x in range(100)):
            min_l= min(min_l , end - begin)
print (min_l)