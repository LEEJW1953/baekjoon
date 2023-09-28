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
            cost = dis+tmp[1]
            if cost<d[tmp[0]]:
                d[tmp[0]]=cost
                heappush(q, (cost, tmp[0]))

v, e = map(int, input().split())
start=int(input())
INF=1e12
g=[[] for _ in range(v+1)]
d=[INF]*(v+1)
for i in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
dik(start)
for i in d[1:]:
    if i==INF:
        print('INF')
    else:
        print(i)