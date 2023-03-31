import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, y):
    q=deque()
    q.append([x, y])
    vis[x][y]=1
    arr=[[x, y]]
    total=g[x][y]
    count=1
    while q:
        [xx, yy]=q.popleft()
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if (l<=abs(g[xx][yy]-g[nx][ny])<=r) and not vis[nx][ny]:
                    total+=g[nx][ny]
                    arr.append([nx, ny])
                    count+=1
                    vis[nx][ny]=1
                    q.append([nx, ny])
    if len(arr)!=1:
        return [arr, total, count]
    else:
        return []

n, l, r = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer=0
while True:
    vis=[[0]*n for _ in range(n)]
    tmp=[]
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                tmp1=bfs(i, j)
                if tmp1:
                    tmp.append(tmp1)
    if not tmp:
        break
    for i in range(len(tmp)):
        val=tmp[i][1]//tmp[i][2]
        for j in tmp[i][0]:
            g[j[0]][j[1]]=val
    answer+=1
print(answer)