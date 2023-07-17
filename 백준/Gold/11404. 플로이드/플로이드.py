import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
INF=1e10
g=[[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    g[i][i]=0
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b]=min(c, g[a][b])
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            g[j][k]=min(g[j][k], g[j][i]+g[i][k])
for i in range(1, n+1):
    for j in range(1, n):
        if g[i][j]!=INF:
            print(g[i][j], end=' ')
        else:
            print(0, end=' ')
    if g[i][-1]!=INF:
        print(g[i][-1])
    else:
        print(0)