import sys
input=sys.stdin.readline

def boom(x, y, nx1, nx2, ny1, ny2):
    if 0<=nx1<n and 0<=nx2<n and 0<=ny1<m and 0<=ny2<m and not vis[x][y] and not vis[nx1][ny1] and not vis[nx2][ny2]:
        return wood[x][y]*2+wood[nx1][ny1]+wood[nx2][ny2]
    return 0

def boomerang(x, y, total):
    global ans
    if ans<total:
        ans=total
    for i in range(x, n):
        for j in range(m):
            if i==x and j<y:
                continue
            elif vis[i][j]:
                continue
            else:
                for k in range(4):
                    nx1, ny1, nx2, ny2 = i+new[k][0], j+new[k][1], i+new[k][2], j+new[k][3]
                    t=boom(i, j, nx1, nx2, ny1, ny2)
                    if t:
                        vis[i][j]=1
                        vis[nx1][ny1]=1
                        vis[nx2][ny2]=1
                        boomerang(i, j, total+t)
                        vis[i][j]=0
                        vis[nx1][ny1]=0
                        vis[nx2][ny2]=0
    return

new=[[1, 0, 0, -1], [-1, 0, 0, -1], [-1, 0, 0, 1], [1, 0, 0, 1]]
n, m = map(int, input().split())
wood=[list(map(int, input().split())) for _ in range(n)]
vis=[[0]*m for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        boomerang(i, j, 0)
print(ans)