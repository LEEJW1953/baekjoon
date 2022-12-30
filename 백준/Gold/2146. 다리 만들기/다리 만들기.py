import sys
input=sys.stdin.readline
from collections import deque

def bfs(num):
    q=deque()
    dis=[[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==num:
                dis[i][j]=0
                q.append([j, i])
    
    while q:
        [x, y]=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[ny][nx] and arr[ny][nx]!=num:
                    res.append(dis[y][x])
                    return
                elif (not arr[ny][nx]) and dis[ny][nx]==-1:
                    dis[ny][nx]=dis[y][x]+1
                    q.append([nx, ny])
            else:
                continue

def island(a, b, num):
    q=deque()
    q.append([a, b])
    while q:
        [x, y]=q.popleft()
        arr[y][x]=num
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[ny][nx]==1 and not vis[ny][nx]:
                    vis[ny][nx]=True
                    q.append([nx, ny])
            else:
                continue

n=int(input())
arr=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
vis=[[False]*n for _ in range(n)]
res=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

num=2
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            island(j, i, num)
            num+=1

for i in range(2, num):
    bfs(i)
print(min(res))