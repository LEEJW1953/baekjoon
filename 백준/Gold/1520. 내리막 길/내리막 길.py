import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x==m-1 and y==n-1:
        return 1
    if arr[y][x]!=-1:
        return arr[y][x]
    arr[y][x]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if g[ny][nx]<g[y][x]:
                arr[y][x]+=dfs(nx, ny)
    return arr[y][x]

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
arr=[[-1]*m for _ in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
print(dfs(0, 0))