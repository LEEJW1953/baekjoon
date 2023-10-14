import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y, h):
    q=deque()
    qq=deque()
    q.append([x ,y])
    qq.append([x ,y])
    vis=[[0]*m for _ in range(n)]
    vis[x][y]=1
    while q:
        xx, yy=q.popleft()
        for i in range(8):
            nx, ny=xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if h<g[nx][ny]:
                    return False
                if not vis[nx][ny] and g[nx][ny]==h:
                    q.append([nx, ny])
                    qq.append([nx, ny])
                    vis[nx][ny]=1
    while qq:
        [xx, yy]=qq.popleft()
        v[xx][yy]=1
    return True

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, 1, 1, -1, -1, -1, 0, 0]
dy=[1, 0, -1, 1, 0, -1, 1 ,-1]
v=[[0]*m for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if g[i][j] and not v[i][j]:
            if bfs(i, j, g[i][j]):
                ans+=1
print(ans)