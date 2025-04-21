from ipaddress import*
for m in range(255):
    ip1=ip_network(f"200.154.190.12/{m}",0)
    ip2=ip_network(f"200.154.184.0/{m}",0)
    if ip1==ip2:
        print(m)