import sys
input=sys.stdin.readline
from collections import deque

def BFS():
    while q:
        [x, y] = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if arr[ny][nx]==0:
                arr[ny][nx]=arr[y][x]+1
                q.append([nx, ny])
    return

m, n=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
q=deque()
result=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            q.append([j, i])
BFS()
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            print(-1)
            exit(0)
    result=max(result, max(arr[i]))
print(result-1)