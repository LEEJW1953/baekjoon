import sys
input=sys.stdin.readline
from collections import deque

def BFS(j, i):
    q=deque()
    q.append([j, i])
    while q:
        [x, y] = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visit[ny][nx]:
                visit[ny][nx]=False
                q.append([nx, ny])
    return

n=int(input())
arr=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
for i in range(n):
    arr.append(list(map(int, input().split())))
res=[]
h=0
while True:
    count=0
    visit=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]>h:
                visit[j][i]=True
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
               BFS(j, i)
               count+=1
    res.append(count)
    h+=1
    if count==0:
        break
print(max(res))