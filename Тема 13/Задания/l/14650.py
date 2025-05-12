from ipaddress import *

for mask in range(32):
    net1=ip_network(f"216.54.187.235/{mask}",0)
    net2=ip_network(f"216.54.174.128/{mask}",0)
    if (net1[0]!=net2[0]and ip_address("216.54.187.235")!=net1[0] and ip_address("216.54.187.235")!=net1[-1 ] and
        ip_address("216.54.174.128") != net2[0] and ip_address("216.54.174.128") != net2[-1]):
        print(mask)