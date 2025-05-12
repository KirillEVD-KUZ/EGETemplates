k=0
for i in range(68719476736,549755813888):
    vs=""
    x=i
    while x >0:
        vs+=str(x%8)
        x//=8
    a=vs[::-1]
    if len(a)==12 and ((a.count("1")+a.count("3")+a.count("5")+a.count("7"))==3) and ("11" not in a) and ("13" not in a)and ("15" not in a)and ("17" not in a)and ("31" not in a)and ("31" not in a)and ("35" not in a)and ("37" not in a) and ("51" not in a)and ("53" not in a)and ("55" not in a)and ("57" not in a) and ("71" not in a)and ("73" not in a)and ("75" not in a)and ("77" not in a):
        k+=1
print(k)