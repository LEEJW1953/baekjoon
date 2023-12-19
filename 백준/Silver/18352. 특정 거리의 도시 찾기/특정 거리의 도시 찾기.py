import sys
input=sys.stdin.readline
from heapq import heappop, heappush

def dik(x):
    q=[]
    for i in g[x]:
        heappush(q, (1, i))
        d[i]=1
    while q:
        dis, node = heappop(q)
        for i in g[node]:
            cost = dis+1
            if cost<d[i]:
                heappush(q, (cost, i))
                d[i]=cost
    return

n, m, k, x = map(int, input().split())
g=[[] for _ in range(n+1)]
INF=1e9
d=[INF]*(n+1)
d[x]=0
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
dik(x)
ans=[]
for i in range(1, n+1):
    if d[i]==k:
        ans.append(i)
if ans:
    print(*ans)
else:
    print(-1)