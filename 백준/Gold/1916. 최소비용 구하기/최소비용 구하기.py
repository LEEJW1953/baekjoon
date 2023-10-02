import sys
input=sys.stdin.readline
from heapq import heappop, heappush

def dik(start):
    q=[]
    heappush(q, (0, start))
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

n=int(input())
m=int(input())
INF=1e12
d=[INF]*(n+1)
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
start, end = map(int,input().split())
dik(start)
print(d[end])