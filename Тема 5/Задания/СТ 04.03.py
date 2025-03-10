mx=0
for n in range(1,100000):
    b = bin(n)[2:]
    if b.count('0') > b.count('1'):
        # Преобразуем строку в список для изменения
        b_list = list(b)
        for i in range(len(b_list)):
            if b_list[i] == '0':
                b_list[i] = '1'  # Заменяем первый ноль на единицу
                break
        b = ''.join(b_list)  # Возвращаемся к строке
    else:
        # Переворачиваем строку и преобразуем в список
        b_reversed = list(b[::-1])
        for q in range(len(b_reversed)):
            if b_reversed[q] == '1':
                b_reversed[q] = '0'  # Заменяем первую единицу на ноль
                break
        b = ''.join(b_reversed[::-1])  # Возвращаем обратный порядок
    res = int(b, 2)
    res1=abs(n-res)
    if mx<res1:
        mx=res1
        print(n,mx)

