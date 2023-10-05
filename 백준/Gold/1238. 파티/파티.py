import sys
input=sys.stdin.readline
from heapq import heappop, heappush

def dik(start):
    q=[]
    heappush(q, (0, start))
    d=[INF]*(n+1)
    d[start]=0
    while q:
        dis, node = heappop(q)
        if d[node]<dis:
            continue
        for tmp in g[node]:
            cost=tmp[1]+dis
            if cost<d[tmp[0]]:
                d[tmp[0]]=cost
                heappush(q, (cost, tmp[0]))
    return d

n, m, x = map( int, input().split())
INF=1e12
g=[[] for _ in range(n+1)]
ans=0
for i in range(m):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
home=dik(x)
for i in range(1, n+1):
    d=[INF]*(n+1)
    dis=dik(i)
    ans=max(ans, dis[x]+home[i])
print(ans)