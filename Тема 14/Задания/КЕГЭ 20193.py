"""for x in "0123456789ABCDEFGH":
    a=int(f"11H{x}05",18)
    b=int(f"3F{x}54{x}8",18)
    c=int(f"G{x}{x}{x}9", 18)
    if (a+b+c)%14==0:
        print(x, (a+b+c)//14)
2 9600497"""
a = (15625 ** 16) - ((3125 ** 3) * (25 ** 19)) + (625 ** 4) - 2005
dp = ""
k=0
while a > 0:
    if a%25==0:
        k+=1
    a=a//25
print(k)