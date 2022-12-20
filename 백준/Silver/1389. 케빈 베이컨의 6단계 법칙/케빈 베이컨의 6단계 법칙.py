import sys
input=sys.stdin.readline
from collections import deque

def bfs(x):
    vis=[0]*(n+1)
    q.append(x)
    vis[x]=1
    while q:
        nx=q.popleft()
        for i in g[nx]:
            if not vis[i]:
                vis[i]=vis[nx]+1
                q.append(i)
    return sum(vis)

n, m = map(int, input().split())
g=[[]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y=map(int, input().split())
    g[x].append(y)
    g[y].append(x)
q=deque()
res=[]
for i in range(1, n+1):
    res.append(bfs(i))
print(res.index(min(res))+1)