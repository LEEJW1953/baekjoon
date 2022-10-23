import sys
from collections import deque
input=sys.stdin.readline

def bfs(arr, x, y):
    q=deque()
    q.append([x, y])
    arr[y][x]=0
    while q:
        [x, y] = q.popleft()
        # print(count, x, y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if arr[ny][nx]==1:
                arr[ny][nx]=0
                q.append([nx, ny])
    return

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
t=int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    arr=[[0]*m for _ in range(n)]
    count=0
    for j in range(k):
        x, y=map(int, input().split())
        arr[y][x]=1
    for j in range(n):
        for k in range(m):
            if arr[j][k]==1:
                bfs(arr, k, j)
                count+=1
    print(count)