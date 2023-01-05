sq = [i * i for i in range(1, 320)]

N = int(input())

if N in sq: print(1)
else:
    for i in sq:
        for j in sq:
            if i + j == N: print(2); exit()
    while N % 4 == 0:
        N //= 4
    if N % 8 == 7: print(4)
    else: print(3)