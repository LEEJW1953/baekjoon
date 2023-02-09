import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    global chz, count
    count+=1
    chz=0
    arr=[[0]*m for _ in range(n)]
    vis=[[0]*m for _ in range(n)]
    q=deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if g[ny][nx]==0 and not vis[ny][nx]:
                    q.append([nx, ny])
                    vis[ny][nx]=1
                elif g[ny][nx]==1 and not vis[ny][nx]:
                    arr[ny][nx]=1
                    vis[ny][nx]=1
    for i in range(n):
        for j in range(m):
            g[i][j]-=arr[i][j]
    for i in range(n):
        chz+=sum(g[i])
    ans.append([count, chz])


dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
count=0
ans=[]
chz=0
for i in range(n):
    chz+=sum(g[i])
ans.append([count, chz])
while chz:
    bfs()
print(ans[-1][0])
print(ans[-2][1])