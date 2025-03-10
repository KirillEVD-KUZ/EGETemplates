from ipaddress import*
for m in range(10,33):
    n1=ip_network(f"200.154.190.12/{m}",0)
    n2=ip_network(f"200.154.184.0/{m}",0)
    if n1==n2:
        print(n1)