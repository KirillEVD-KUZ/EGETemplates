import ipaddress
from ipaddress import ip_network
k=0
net=ip_network("235.53.0.0/255.255.224.0",0)
for ip in net:
    b=bin(int(ip))[2:]
    if b.count("1")%5==0:
        if str(b)[-3:]=="110":
            k+=1
print(k)