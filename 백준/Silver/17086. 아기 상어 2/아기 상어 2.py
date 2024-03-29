import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    while q:
        [xx, yy] = q.popleft()
        for i in range(8):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<m and not g[nx][ny]:
                g[nx][ny]=g[xx][yy]+1
                q.append([nx, ny])

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, -1, 1, -1, 1, -1, 0, 0]
dy=[0, 0, 1, 1, -1, -1, 1, -1]
ans=0
q=deque()
for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            q.append([i, j])
bfs()
for i in range(n):
    ans=max(ans, max(g[i]))
print(ans-1)