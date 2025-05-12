
s=[]
for a1 in range(1,200):
    for a2 in range(1,200):
        f1=True
        for x in range(1,200):
            if not((117<=x<=159)<=(((not(a1<=x<=a2)) and (130<=x<=181)) <= (not(117<=x<=159)))):
                f=False
                break
        if f1:
            s.append(a2-a1)
print(min(s))
