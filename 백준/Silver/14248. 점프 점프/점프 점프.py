import sys
input=sys.stdin.readline
from collections import deque

def bfs(x):
    q=deque()
    vis=[0]*(n)
    vis[x]=1
    q.append(x)
    while q:
        xx=q.pop()
        nx1, nx2 = xx+g[xx], xx-g[xx]
        if 0<=nx1<n and not vis[nx1]:
            q.append(nx1)
            vis[nx1]=1
        if 0<=nx2<n and not vis[nx2]:
            q.append(nx2)
            vis[nx2]=1
    return sum(vis)

n=int(input())
g=list(map(int, input().split()))
s=int(input())
print(bfs(s-1))