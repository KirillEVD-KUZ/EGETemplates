a=list(map(int,open("ЕГКР17558.txt").readlines()))
count_pos=0
count_us=0
mx_sm=0
for q in range(len(a)):
    if a[q]%32==0:
        count_pos+=1
for i in range(len(a)-1):
    if a[i]<0 or a[i+1]<0:
        if a[i]+a[i+1]<count_pos:
            count_us+=1
            if (a[i]+a[i+1])>mx_sm:
                mx_sm=a[i]+a[i+1]
print(count_us, mx_sm)