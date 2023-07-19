import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
g=[[1e9]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            g[i][j]=1
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j]=min(g[i][j], g[i][k]+g[k][j])
for i in range(n):
    for j in range(n):
        if g[i][j]==1e9:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()