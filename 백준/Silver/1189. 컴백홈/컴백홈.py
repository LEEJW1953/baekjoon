import sys
input=sys.stdin.readline

def dfs(x, y, d):
    global ans
    if x==0 and y==c-1 and d==k-1:
        ans+=1
        return
    if d>k-1:
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if g[nx][ny]=='.' and not vis[nx][ny]:
                vis[nx][ny]=1
                dfs(nx, ny, d+1)
                vis[nx][ny]=0

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
r, c, k = map(int, input().split())
g=[list(input().strip()) for _ in range(r)]
vis=[[0]*c for _ in range(r)]
ans=0
vis[r-1][0]=1
dfs(r-1, 0, 0)
print(ans)