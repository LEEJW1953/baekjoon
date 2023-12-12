import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
m=int(input())
g=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
q=deque()
vis=[0]*(n+1)
vis[1]=1
for i in g[1]:
    q.append(i)
    vis[i]=1
while q:
    x=q.popleft()
    for i in g[x]:
        vis[i]=1
print(sum(vis)-1)