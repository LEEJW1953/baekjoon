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
            if nx==0 and ny==0:
                continue
            if arr[ny][nx]==1:
                arr[ny][nx]=arr[y][x]+1
                q.append([nx, ny])
    return

n, m=map(int, input().split())
arr=[]
for i in range(n):
    arr1=[]
    for j in input().strip():
        arr1.append(int(j))
    arr.append(arr1)
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
q=deque()
q.append([0, 0])
result=0
BFS()
print(arr[-1][-1])