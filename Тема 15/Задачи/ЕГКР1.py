for A in range(100000):
    B = True
    for x in range(10000):
        # Логика формулы:
        # (x & 5160 > 0 or x & 3650 > 0) → (x & 9545 == 0 → x & A > 0)
        # Это эквивалентно:
        # not(x & 5160 > 0 or x & 3650 > 0) or (x & 9545 != 0 or x & A > 0)
        if (x & 5160 > 0 or x & 3650 > 0) and not (x & 9545 != 0 or x & A > 0):
            B = False
            break  # Прерываем внутренний цикл, если формула нарушена
    if B:
        print(A)
        break