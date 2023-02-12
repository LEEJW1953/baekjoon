import sys
input=sys.stdin.readline
from collections import deque

def bfs(a,b):
    global next
    tmp=0
    q=deque()
    q.append([a, b])
    vis=[[0]*6 for _ in range(12)]
    vis[b][a]=1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<6 and 0<=ny<12:
                if g[ny][nx]==g[b][a] and not vis[ny][nx]:
                    q.append([nx, ny])
                    vis[ny][nx]=1
    for i in range(12):
        tmp+=sum(vis[i])
    if tmp>=4:
        for i in range(12):
            for j in range(6):
                if vis[i][j]:
                    result.append([j, i])
    return

def move():
    for i in range(6):
        arr=[]
        for j in range(11, -1, -1):
            if g[j][i]!=".":
                arr.append(g[j][i])
        for j in range(12):
            if arr:
                g[11-j][i]=arr.pop(0)
            else:
                g[11-j][i]='.'
    return

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
count=0
next=True
g=[list(input().strip()) for _ in range(12)]
while next:
    result=[]
    for i in range(12):
        for j in range(6):
            if g[i][j]!='.':
                bfs(j, i)
    if result:
        count+=1
        for i in result:
            g[i[1]][i[0]]='.'
        move()
    else:
        next=False
print(count)