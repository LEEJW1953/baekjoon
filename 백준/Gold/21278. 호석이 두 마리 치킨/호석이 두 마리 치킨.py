import sys
input=sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
INF=int(1e9)
c1, c2=0, 0
ans=INF
g=[[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            g[i][j]=0
for i in range(m):
    a, b = map(int, input().split())
    g[a][b]=1
    g[b][a]=1
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j]=min(g[i][j], g[i][k]+g[k][j])
for i in combinations(range(1, n+1), 2):
    tmp=0
    for j in range(1, n+1):
        tmp+=2*min(g[j][i[0]], g[j][i[1]])
    if tmp<ans:
        c1, c2 = i[0], i[1]
        ans=tmp
print(c1, c2, ans)