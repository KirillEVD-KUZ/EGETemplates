for 
if N % 2==0:
    b="11" + bin(N)[2:]
else:
    b= "1" + bin(N)[2:] + "10"
res= int(b,2)
print (res)