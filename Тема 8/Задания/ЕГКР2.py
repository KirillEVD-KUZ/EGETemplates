"""Сколько существует натуральных чисел, не превышающих 738 000 000,
запись которых в системе счисления с основанием 14 содержит ровно 8
различных цифр?"""
count=0
for i in range(1,738000000):
    n= i
    ct=""
    sp=[]
    while n>0:
        ost=n%14
        ct+=str(ost)
        n=n//14
    for a in range(len(ct)):
        if ct[a] not in sp:
            sp.append(ct[a])
    if len(sp) == 8:
        count+=1
print(count)