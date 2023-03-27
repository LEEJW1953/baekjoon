import sys
input=sys.stdin.readline
from collections import deque

def bfs(xx, yy):
    global ate, time
    q=deque()
    q.append([xx, yy])
    vis=[[-1]*n for _ in range(n)]
    vis[stx][sty]=0
    arr=[]
    while q:
        [x, y]=q.popleft()
        if 0<g[x][y]<size and g[x][y]!=9:
            if not arr:
                mindis=vis[x][y]
                arr.append([x, y])
            else:
                if vis[x][y]<=mindis:
                    arr.append([x, y])
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if vis[nx][ny]==-1 and g[nx][ny]<=size:
                    vis[nx][ny]=vis[x][y]+1
                    q.append([nx, ny])
    if arr:
        arr.sort()
        ate+=1
        time+=vis[arr[0][0]][arr[0][1]]
        g[xx][yy]=0
        g[arr[0][0]][arr[0][1]]=9
        return arr[0]
    return [xx, yy]

dx=[-1, 0, 0, 1]
dy=[0, -1, 1, 0]
n=int(input())
g=[list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j]==9:
            [stx, sty] = [i, j]
size=2
ate=0
time=0
while True:
    tmp=bfs(stx, sty)
    if tmp==[stx, sty]:
        break
    if size==ate:
        size+=1
        ate=0
    [stx, sty]=tmp
print(time)