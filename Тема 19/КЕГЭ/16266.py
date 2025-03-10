def game(heap, moves, to):
    if heap < 20:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap - 10, moves + 1, to),
         game(heap // 2, moves + 1, to)]
    return any(h)
print("19-", max(s for s in range(30,10000) if ))