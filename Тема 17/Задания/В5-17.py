
text=list(map(int,open("В5-17.txt").readlines()))
k=0
for i in range(len(text)-1):
    smdel1=0
    for y in range(1,len(str(text[i]))):
        if text[i]%y==0:
           smdel1+=y
    smdel2=0
    for t in range(1,len(str(text[i+1]))):
        if text[i+1]%y==0:
           smdel2+=t
    if (smdel1+smdel2)%12==0:
        k+=1
print(k)