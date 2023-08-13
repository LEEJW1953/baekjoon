import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y):
    global tx, ty
    q=deque()
    q.append([x, y, 0])
    vis=[[0]*m for _ in range(n)]
    vis[x][y]=1
    while q:
        [xx, yy, dd]=q.popleft()
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny] and not vis[nx][ny]:
                    g[nx][ny]=dd+1
                    vis[nx][ny]=1
                    q.append([nx, ny, dd+1])

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, -1, 0 ,0]
dy=[0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if g[i][j]==2:
            g[i][j]=0
            tx, ty = i, j
bfs(tx, ty)
for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            if i==tx+1 and j==ty:
                continue
            if i==tx-1 and j==ty:
                continue
            if i==tx and j==ty+1:
                continue
            if i==tx and j==ty-1:
                continue
            else:
                g[i][j]=-1
for i in range(n):
    print(*g[i])