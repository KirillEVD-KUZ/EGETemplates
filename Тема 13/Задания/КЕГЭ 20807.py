from ipaddress import*
k=0
a=ip_network("172.16.192.0/255.255.192.0",0)
for i in a:
    b=bin(int(i))[2:]
    if str(b).count("1")%5!=0:
        k+=1
print(k)