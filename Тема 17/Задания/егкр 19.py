a = list(map(int, open("17 (3).txt").readlines()))
mn = 100000
sp=[]
for u in range(len(a)):
    if (0 < a[u]) and (a[u] < mn):
        mn = a[u]
for i in range(len(a) - 2):
    if ((len(str(abs(a[i])))==4 and a[i] % 10 == 6) + (len(str(abs(a[i+1])))==4 and a[i + 1] % 10 == 6) + (
            len(str(abs(a[i+2]))) == 4 and a[i + 2] % 10 == 6)) == 1:
        if (a[i]+a[i+1]+a[i+2])<mn:
            sp.append(a[i]+a[i+1]+a[i+2])
print(len(sp), max(sp),mn)
