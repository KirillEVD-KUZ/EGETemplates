from ipaddress import*
ip=ip_network("172.16.192.0/255.255.192.0", 0)
k=0
for n in ip:
    b=bin(int(n))[2:]
    if b.count("1")%5!=0:
        k+=1
print(k)