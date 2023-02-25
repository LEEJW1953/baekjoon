import sys
input=sys.stdin.readline

def dfs(x, y, k, tmp):
    global ans
    if ans>=tmp+maxx*(4-k):
        return
    if k==4:
        ans=max(ans, tmp)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and not vis[nx][ny]:
            if k==2:
                vis[nx][ny]=1
                dfs(x, y, k+1, tmp+g[nx][ny])
                vis[nx][ny]=0
            vis[nx][ny]=1
            dfs(nx, ny, k+1, tmp+g[nx][ny])
            vis[nx][ny]=0

n, m = map(int, input().split())
g=[list(map(int, input().split())) for i in range(n)]
vis=[[0]*m for _ in range(n)]
ans = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, -1]
maxx=max(map(max, g))
for i in range(n):
    for j in range(m):
        vis[i][j]=1
        dfs(i, j, 1, g[i][j])
        vis[i][j]=0
print(ans)