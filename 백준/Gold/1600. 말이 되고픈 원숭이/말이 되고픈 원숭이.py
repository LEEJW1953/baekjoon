import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append([0, 0, 0])
    vis[0][0][0]=1
    while q:
        [x, y, z]=q.popleft()
        if x==w-1 and y==h-1:
            res.append(vis[y][x][z])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<w and 0<=ny<h:
                if not g[ny][nx] and not vis[ny][nx][z]:
                    vis[ny][nx][z]=vis[y][x][z]+1
                    q.append([nx, ny, z])
            else:
                continue
        for i in range(8):
            nx=x+hx[i]
            ny=y+hy[i]
            nz=z+1
            if 0<=nx<w and 0<=ny<h and nz<=k:
                if not g[ny][nx] and not vis[ny][nx][nz]:
                    vis[ny][nx][nz]=vis[y][x][z]+1
                    q.append([nx, ny, nz])
            else:
                continue

k=int(input())
w, h=map(int, input().split())
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
hx=[1, 1, 2, 2, -1, -1, -2, -2]
hy=[2, -2, 1, -1, 2, -2, 1, -1]
g=[]
res=[]
vis=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]
for i in range(h):
    g.append(list(map(int, input().split())))
bfs()
if res:
    print(min(res)-1)
else:
    print(-1)