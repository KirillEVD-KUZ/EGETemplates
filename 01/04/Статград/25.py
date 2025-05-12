for x in range(1750000,5000000):
    dlp=[]
    for i in range(1,x):
        prst=[]
        for q in range(1,i+1):
            if i%q==0:
                prst.append(q)
        if len(prst)==2:
            dlp.append(i)
    mx=max(dlp)
    if mx<=15000 and mx%10==7:
        print(x)