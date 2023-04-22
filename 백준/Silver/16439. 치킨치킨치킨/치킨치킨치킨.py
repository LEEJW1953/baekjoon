import sys
input=sys.stdin.readline
from itertools import combinations

def f():
    maxtotal = 0
    for i in combinations(range(m), 3):
        total = 0
        for j in range(n):
            arr=[]
            for k in range(3):
                arr.append(g[j][i[k]])
            total+=max(arr)
        maxtotal = max(maxtotal, total)
    return maxtotal

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
ans = 0
print(f())