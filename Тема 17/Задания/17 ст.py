a = list(map(int, open("st.txt").readlines()))
mi = min(a) % 5
mx = max(a) % 7
count = 0
sm=[]
for i in range(len(a) - 2):
    if 1000 <= a[i] < 10000 or 1000 <= a[i + 1] < 10000 or 1000 <= a[i + 2] < 10000:
        if int(a[i] % 5 == mi) + int(a[i + 1] % 5 == mi) + int(a[i + 2] % 5 == mi) <= 1:
            if int(a[i] % 7 == mx) + int(a[i + 1] % 7 == mx) + int(a[i + 2] % 7 == mx) >= 2:
                count+=1
                sm.append(a[i] + a[i+1] + a[i+2])

print(count)
print(max(sm))