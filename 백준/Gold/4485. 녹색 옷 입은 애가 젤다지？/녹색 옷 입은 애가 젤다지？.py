import sys
input=sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(g, n):
    q=[]
    vis=[[INF]*n for _ in range(n)]
    vis[0][0]=g[0][0]
    heappush(q, (g[0][0], [0, 0]))
    while q:
        distance, node = heappop(q)
        if vis[node[0]][node[1]]<distance:
            continue
        for i in range(4):
            nx, ny = node[0]+dx[i], node[1]+dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost=distance+g[nx][ny]
                if cost<vis[nx][ny]:
                    vis[nx][ny]=cost
                    heappush(q, (cost, [nx, ny]))
    return vis

INF=int(1e9)
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
i=1
while True:
    n=int(input())
    if n==0:
        break
    g=[list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {i}:',dijkstra(g, n)[-1][-1])
    i+=1