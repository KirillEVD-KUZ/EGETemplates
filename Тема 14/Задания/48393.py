for x in "01234567":
    for y in "01234567":
        res=int(f"{y}04{x}5",11) + int(f"253{x}{y}", 8)
        if res%117==0:
            print(res//117)
            break
