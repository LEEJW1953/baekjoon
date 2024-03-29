import sys
input=sys.stdin.readline
from collections import deque

def bfs1(x, y):
    arr3=[]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and vis[ny][nx]:
            arr3.append([nx, ny])
    return arr3

def switch():
    q=deque()
    q.append([0, 0])
    arr[0][0]=1
    while q:
        [x, y]=q.popleft()
        for i in s[y][x]:
            [nx, ny]=i
            if not arr[ny][nx]:
                arr[ny][nx]=1
                arr1=bfs1(nx, ny)
                if arr1:
                    for i in arr1:
                        q.append(i)
                        vis[i[1]][i[0]]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[ny][nx] and not vis[ny][nx]:
                q.append([nx, ny])
                vis[ny][nx]=1

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
n, m=map(int, input().split())
arr=[[0]*n for _ in range(n)]
vis=[[0]*n for _ in range(n)]
res=0
s=[[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, a, b=map(int, input().split())
    s[y-1][x-1].append([a-1, b-1])
switch()
for i in range(n):
    res+=sum(arr[i])
print(res)