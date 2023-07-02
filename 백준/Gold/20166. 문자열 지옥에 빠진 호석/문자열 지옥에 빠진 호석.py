import sys
input=sys.stdin.readline

def dfs(x, y, s, t):
    global count
    if s==t:
        count+=1
        return
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0:
            nx=n-1
        if ny<0:
            ny=m-1
        if nx==n:
            nx=0
        if ny==m:
            ny=0
        if g[nx][ny]==t[len(s)]:
            s+=g[nx][ny]
            dfs(nx, ny, s, t)
            s=s[:-1]

dx=[1, -1, 0, 0, -1, -1, 1, 1]
dy=[0, 0, 1, -1, -1, 1, -1, 1]
n, m, k = map(int, input().split())
g=[list(input().strip()) for _ in range(n)]
arr=[input().strip() for _ in range(k)]
d={}
for l in range(k):
    count=0
    if arr[l] not in d:
        for i in range(n):
            for j in range(m):
                if g[i][j]==arr[l][0]:
                    dfs(i, j, g[i][j], arr[l])
        d[arr[l]]=count
    print(d[arr[l]])