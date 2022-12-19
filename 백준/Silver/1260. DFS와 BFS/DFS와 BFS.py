import sys
input=sys.stdin.readline
from collections import deque

sys.setrecursionlimit(111111)

def dfs(x):
    print(x, end=' ')
    vis[x]=True
    for i in range(1, n+1):
        if not vis[i] and g[x][i]==1:
            dfs(i)

def bfs(x):
    q=deque()
    q.append(x)
    vis[x]=False
    while q:
        y=q.popleft()
        print(y, end=' ')
        for i in range(1, n+1):
            if vis[i] and g[y][i]==1:
                q.append(i)
                vis[i]=False

n, m, v=map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    g[y][x]=g[x][y]=1
vis=[False]*(n+1)
dfs(v)
print()
bfs(v)
# print(' '.join(list(map(str, dres))))
# print(' '.join(list(map(str, bres))))