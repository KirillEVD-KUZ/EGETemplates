def divs_count(n):
    divs = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    return sorted(divs, reverse=True)


for q in range(460000001, 470000000):
    divs = divs_count(q)
    if len(divs)>=5:
        print(divs[4])

