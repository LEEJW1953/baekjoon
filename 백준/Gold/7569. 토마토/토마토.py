import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    tmp=1
    res=0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if t[i][j][k]==1:
                    q.append([k, j, i])
                if t[i][j][k]==0:
                    tmp=0
    if tmp:
        print(0)
    else:
        while q:
            [x, y, z]=q.popleft()
            for i in range(6):
                nx=x+dx[i]
                ny=y+dy[i]
                nz=z+dz[i]
                if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                    if t[nz][ny][nx]==0 and not vis[nz][ny][nx]:
                        t[nz][ny][nx]=t[z][y][x]+1
                        vis[nz][ny][nx]=1
                        q.append([nx, ny, nz])
                        res=max(res, t[z][y][x])

        for i in range(h):
            for j in range(n):
                for k in range(m):
                    if t[i][j][k]==0:
                        print(-1)
                        exit(0)
        print(res)

m, n, h=map(int, input().split())
t=[]
dx=[1, -1, 0, 0, 0, 0]
dy=[0, 0, 1, -1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]
vis=[[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    t1=[]
    for j in range(n):
        t1.append(list(map(int, input().split())))
    t.append(t1)
bfs()