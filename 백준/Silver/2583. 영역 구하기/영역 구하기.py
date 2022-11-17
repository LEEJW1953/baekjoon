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
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[ny][nx]==0:
                arr[ny][nx]=1
                count+=1
                q.append([nx, ny])
    return count

m, n, k = map(int, input().split())
arr=[[0]*n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res=[]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2, 1):
        for j in range(y1, y2, 1):
            arr[j][i]=1
for i in range(m):
    for j in range(n):
        if arr[i][j]==0:
            arr[i][j]=1
            res.append(BFS(j, i))
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i], end=' ')