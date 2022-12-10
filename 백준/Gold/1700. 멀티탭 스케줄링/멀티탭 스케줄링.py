N, K = map(int, input().split())
scheduling = list(map(int, input().split()))

adaptor = [0] * N
count = 0
scheduling_idx = 0
tmp = 0
tmp_i = 0

for i in scheduling:
    if i in adaptor:
        pass
    elif 0 in adaptor:
        adaptor[adaptor.index(0)] = i
    else:
        for j in adaptor:
            if j not in scheduling[scheduling_idx:]:
                tmp = j
                break
            elif scheduling[scheduling_idx:].index(j) > tmp_i:
                tmp = j
                tmp_i = scheduling[scheduling_idx:].index(j)
        adaptor[adaptor.index(tmp)] = i
        tmp = tmp_i = 0
        count += 1
    scheduling_idx += 1

print(count)