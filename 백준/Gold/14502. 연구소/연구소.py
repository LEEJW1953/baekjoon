import sys
input=sys.stdin.readline
from itertools import combinations
from copy import deepcopy
from collections import deque

def virus(wall):
    global answer
    board=[arr[:] for arr in g]
    for i in range(3):
        board[blank[wall[i]][0]][blank[wall[i]][1]]=1
    q=deque()
    vis=[[0]*m for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==2:
                q.append([i, j])
                vis[i][j]=1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and not vis[nx][ny]:
                board[nx][ny]=2
                q.append([nx, ny])
                vis[nx][ny]=1
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                count+=1
    answer=max(answer, count)
    return


n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
blank=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
answer=0
for i in range(n):
    for j in range(m):
        if g[i][j]==0:
            blank.append([i, j])
for i in combinations(range(len(blank)), 3):
    virus(i)
print(answer)