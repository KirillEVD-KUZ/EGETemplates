mx=0
from ipaddress import*
for m in range(33):
    ip=ip_network(f"145.46.8.250/{m}",0)
    if str(ip.network_address) == "145.46.0.0":
        for ip in ip_network(f"145.46.0.0/{m}",0).hosts():
            b=bin(int(ip))[2:]
            if b.count("1")>mx:
                mx=b.count("1")
        print(mx)
