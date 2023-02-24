import sys
input=sys.stdin.readline
from collections import deque

def dfs(x, y, k, tmp):
    global ans
    if k==4:
        ans=max(ans, tmp)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and not vis[nx][ny]:
            vis[nx][ny]=1
            dfs(nx, ny, k+1, tmp+g[nx][ny])
            vis[nx][ny]=0

def other(x, y):
    global ans
    for i in range(4):
        nx, ny = [x], [y]
        for j in range(4):
            if i!=j:
                nx.append(x+dx[j])
                ny.append(y+dy[j])
        tmp=True
        for j in range(4):
            if nx[j]<0 or n<=nx[j] or ny[j]<0 or m<=ny[j]:
                tmp=False
                break
        if tmp:
            tmp1=0
            for j in range(4):
                tmp1+=g[nx[j]][ny[j]]
            ans=max(ans, tmp1)
    return

n, m = map(int, input().split())
g=[list(map(int, input().split())) for i in range(n)]
vis=[[0]*m for _ in range(n)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        vis[i][j]=1
        dfs(i, j, 1, g[i][j])
        vis[i][j]=0
        other(i, j)
print(ans)