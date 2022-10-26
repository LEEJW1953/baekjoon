import sys
input=sys.stdin.readline
from collections import deque

def bfs(arr, x, y):
    q=deque()
    q.append([x, y])
    arr[y][x]=0
    count=0
    while q:
        count+=1
        [x, y]=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if arr[ny][nx]==1:
                arr[ny][nx]=0
                q.append([nx, ny])
    return count

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]
n, m = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
count1=0
arr1=[0]
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            count1+=1
            arr1.append(bfs(arr, j, i))
print(count1)
print(max(arr1))