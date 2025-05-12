import ipaddress
from ipaddress import ip_network

for mask in range(32):
    net=ip_network(f"205.154.212.20/{mask}",0)
    print(net, net.netmask)
#224