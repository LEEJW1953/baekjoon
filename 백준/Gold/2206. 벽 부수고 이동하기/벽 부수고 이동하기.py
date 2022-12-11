import sys
input=sys.stdin.readline
from collections import deque

def BFS():
    q=deque()
    q.append([0, 0, 0])
    while q:
        [x, y, z]=q.popleft()
        if x==m-1 and y==n-1:
            return check[y][x][z]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or m<=nx or ny<0 or n<=ny:
                continue
            if arr[ny][nx]==0 and check[ny][nx][z]==0:
                check[ny][nx][z]=check[y][x][z]+1
                q.append([nx, ny, z])
            elif arr[ny][nx]==1 and z==0:
                check[ny][nx][1]=check[y][x][z]+1
                q.append([nx, ny, z+1])
    return -1

n, m = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().strip())))
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
check=[[[0]*2 for _ in range(m)] for _ in range(n)]
check[0][0][0]=1
print(BFS())