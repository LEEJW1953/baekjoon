import sys
input=sys.stdin.readline
from collections import deque

def BFS(j, i):
    q=deque()
    q.append([j, i])
    count=1
    while q:
        [x, y] = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if arr[ny][nx]==1:
                arr[ny][nx]=0
                count+=1
                q.append([nx, ny])
    return count

n = int(input())
arr=[]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res=[]
for _ in range(n):
    arr1=[]
    str=input().strip()
    for i in str:
        arr1.append(int(i))
    arr.append(arr1)
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=0
            res.append(BFS(j, i))
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])