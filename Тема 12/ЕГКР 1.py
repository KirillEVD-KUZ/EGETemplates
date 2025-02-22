import random

original_a = "1" * 1000 + "2" * 1000  # Создаём исходную строку
count = 0
sp=[]
for i in range(10000):  # 10000 итераций
    a = list(original_a)  # Преобразуем строку в список
    random.shuffle(a)  # Перемешиваем
    a = "".join(a)  # Собираем строку обратно

    while "111" in a or "22" in a:  # Пока есть указанные подстроки
        a = a.replace("111", "2", 1)
        a = a.replace("222", "1", 1)
        a = a.replace("221", "1", 1)
        a = a.replace("122", "1", 1)
        a = a.replace("22", "2", 1)

    if a.count("1") == 5 and a not in sp:  # Если осталось ровно 5 единиц
        sp.append(a)
        count += 1

print(count)
