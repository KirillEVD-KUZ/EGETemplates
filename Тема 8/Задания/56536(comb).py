from itertools import product
count_start_CH = 0
count_start_NCH = 0
for sec in product('ЧН', repeat=12):
    sec = ''.join(sec)
    if sec[0] == 'Н' and sec.count('Н') == 3 and sec.count('НН') == 0:
        count_start_CH += 1
    if sec[0] == 'Ч' and sec.count('Н') == 3 and sec.count('НН') == 0:
        count_start_NCH += 1
print(count_start_CH) # Кол-во чисел, подходящий под условия задачи, начинающиеся с Чётного числа
print(count_start_NCH) # Кол-во чисел, подходящий под условия задачи, начинающиеся с Нечётного числа
print(4 ** 12 * count_start_CH + 3 * 4 ** 11 * count_start_NCH)
# 4 ** 12 => 12 мест по 4 числа
# 4 ** 11 => 11 мест по 4 числа
# 3 * => Если начинать с Нечётных, то возможно только 3 цифры на первом месте (без нуля)
