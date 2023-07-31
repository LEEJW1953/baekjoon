import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y):
    q=deque()
    q.append([x, y])
    vis[x][y]=1
    while q:
        xx, yy = q.popleft()
        for i in range(8):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if g[nx][ny] and not vis[nx][ny]:
                    q.append([nx, ny])
                    vis[nx][ny]=1
    return

m, n = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(m)]
vis=[[0]*n for _ in range(m)]
dx=[1, -1, 0, 0, 1, 1, -1, -1]
dy=[0, 0, 1, -1, 1, -1, 1, -1]
count=0
for i in range(m):
    for j in range(n):
        if not vis[i][j] and g[i][j]:
            bfs(i, j)
            count+=1
print(count)