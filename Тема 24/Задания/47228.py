a = open("24.txt").read()
gl = "AO"
sogl = "CDF"
i = 0
count = 0
maks = 0
while i < len(a):
    if a[i] in sogl and a[i + 1] in gl:
        count += 1
        i += 2
        if count > maks:
            maks = count
    else:
        i += 1
        count = 0
    res = max(count, maks)
print(res)
