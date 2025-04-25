text=open("24_2 (2).txt").readline()
text=text.replace("++"," ")
text=text.replace("+-"," ")
text=text.replace("-+"," ")
text=text.replace("--"," ")
text=text.replace("-06","-0 6")
text=text.replace("+06","+0 6")
text=text.replace("-07","-0 7")
text=text.replace("+07","+0 7")
text=text.replace("-08","-0 8")
text=text.replace("+08","+8 8")
text=text.replace("-09","-0 9")
text=text.replace("+09","+0 9")

a=text.split()
sp=[]
mx=0
mk=0
for i in range(len(a)):
        if len(str(a[i]))>2:
                sp.append(a[i])
for q in range(len(sp)):
    if len(sp[q])>mx:
        mx=len(sp[q])
        mk=sp[q]
print(mx,mk)