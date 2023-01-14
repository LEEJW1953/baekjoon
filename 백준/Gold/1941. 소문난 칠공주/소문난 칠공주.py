import sys
input=sys.stdin.readline
from collections import deque

def f(x):
    global res
    if len(p)==7:
        if bfs():
            res+=1
        return
    for i in range(x, 25):
        p.append(i)
        f(i+1)
        p.pop()

def bfs():
    x=p[0]%5
    y=p[0]//5
    q=deque()
    q.append([x, y])
    vis=[[0]*5 for _ in range(5)]
    tmp, c1, c2 = 0, 0, 0
    while q:
        [ax, ay]=q.popleft()
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<5 and 0<=ny<5 and not vis[ny][nx]:
                if (ny*5+nx) in p:
                    q.append([nx, ny])
                    vis[ny][nx]=1
    for i in range(5):
        tmp+=sum(vis[i])
        for j in range(5):
            if vis[i][j]==1:
                if arr[i][j]=='S':
                    c1+=1
                else:
                    c2+=1
    if tmp==7 and c1>c2:
        return True
    else:
        return False

arr=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
res=0
p=[]
for i in range(5):
    arr.append(list(input().strip()))
f(0)
print(res)