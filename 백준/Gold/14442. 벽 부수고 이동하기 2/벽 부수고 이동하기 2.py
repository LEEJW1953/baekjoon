import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append([0, 0, k])
    res[0][0][k]=1
    while q:
        [x, y, z]=q.popleft()
        if x==m-1 and y==n-1:
            return res[y][x][z]
        tmp=res[y][x][z]+1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not arr[ny][nx] and not res[ny][nx][z]:
                    res[ny][nx][z]=tmp
                    q.append([nx, ny, z])
                elif arr[ny][nx] and 0<z and not res[ny][nx][z-1]:
                    res[ny][nx][z-1]=tmp
                    q.append([nx, ny, z-1])
    return -1
    
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
arr=[]
n, m, k=map(int, input().split())
res=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input().strip())))
print(bfs())