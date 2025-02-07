a = open("24_5832.txt").read()
count = 1
maks = 0
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        count += 1
    else:
        maks = max(count, maks)
        count = 1
print(maks)
