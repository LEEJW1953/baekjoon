import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y):
    q=deque()
    q.append((x, y))
    vis={}
    vis[(x, y)]=0
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny]=='L' and (nx, ny) not in vis.keys():
                    vis[(nx, ny)]=vis[(xx, yy)]+1
                    q.append([nx, ny])
    return max(vis.values())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
g=[list(input().strip()) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if g[i][j]=='L':
            ans = max(ans, bfs(i, j))
print(ans)