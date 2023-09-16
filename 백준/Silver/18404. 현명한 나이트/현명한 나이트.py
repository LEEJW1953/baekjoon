import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y):
    q=deque()
    q.append([x-1, y-1])
    while q:
        [xx, yy] = q.popleft()
        for i in range(8):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<n and vis[nx][ny]==-1:
                q.append([nx, ny])
                vis[nx][ny]=vis[xx][yy]+1

n, m = map(int, input().split())
x, y = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(m)]
dx=[-2, -2, -1, -1, 1, 1, 2, 2]
dy=[-1, 1, -2, 2, -2, 2, -1, 1]
vis=[[-1]*n for _ in range(n)]
vis[x-1][y-1]=0
bfs(x, y)
for i,j in arr:
    print(vis[i-1][j-1], end=' ')