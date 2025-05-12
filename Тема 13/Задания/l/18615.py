import ipaddress
from ipaddress import ip_network

for mask in range(16,32):
    net=ip_network(f"143.131.211.37/{mask}",0)
    k = 0
    for net1 in net:
        b=bin(int(net1))[2:]
        if b.count("1")==10:
            k+=1
    if k==15:
        print(mask)
#17