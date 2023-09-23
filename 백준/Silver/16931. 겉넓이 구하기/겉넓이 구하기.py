import sys
input=sys.stdin.readline

def f(x, y, h):
    tmp=2
    for i in range(h):
        for j in range(4):
            nx, ny = x+dx[j], y+dy[j]
            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny]<i+1:
                    tmp+=1
            else:
                tmp+=1
    return tmp

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
ans=0
for i in range(n):
    for j in range(m):
        ans+=f(i, j, g[i][j])
print(ans)