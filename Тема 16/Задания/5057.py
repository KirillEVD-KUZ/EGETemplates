def f(n):
    if n ==0:
        return 0
    if n%2==1:
        return f(n-1) +1
    if n%2==0:
        return f(n/2)

count=0
for i in range(10000000):
    if f(i) == 2:
        count+=1
print(count)