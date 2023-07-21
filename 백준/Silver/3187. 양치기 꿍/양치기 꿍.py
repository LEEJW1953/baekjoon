import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y):
    q=deque()
    q.append([x, y])
    vis[x][y]=1
    k, v = 0, 0
    if g[x][y]=='k':
        k+=1
    if g[x][y]=='v':
        v+=1
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if not vis[nx][ny] and g[nx][ny]!='#':
                    if g[nx][ny]=='v':
                        v+=1
                    elif g[nx][ny]=='k':
                        k+=1
                    vis[nx][ny]=1
                    q.append([nx, ny])
    return k, v

r, c = map(int, input().split())
g=[list(input().strip()) for _ in range(r)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
sheep, wolf = 0, 0
vis=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if g[i][j]!='#' and not vis[i][j]:
            k, v = bfs(i, j)
            if v<k:
                sheep+=k
            else:
                wolf+=v
print(sheep, wolf)