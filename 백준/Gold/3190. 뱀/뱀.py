import sys
input=sys.stdin.readline
from collections import deque

def direction(time):
    global d
    for i in range(l):
        if time==int(move[i][0]):
            if move[i][1]=="L":
                d-=1
                if d<0:
                    d=3
            elif move[i][1]=="D":
                d+=1
                if d>3:
                    d=0
    return d

n=int(input())
k=int(input())
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
x, y, d = 0, 0, 0
q=deque()
q.append([0, 0])
g=[[0]*n for _ in range(n)]
g[0][0]=2
for i in range(k):
    a, b = map(int, input().split())
    g[a-1][b-1]=1
l=int(input())
move = [list(map(str, input().split())) for _ in range(l)]
tmp=0
while True:
    nx, ny = x+dx[d], y+dy[d]
    if nx<0 or ny<0 or n<=nx or n<=ny or g[nx][ny]==2:
        tmp+=1
        break
    if g[nx][ny]==0:
        g[nx][ny]=2
        q.append([nx, ny])
        end=q.popleft()
        g[end[0]][end[1]]=0
    elif g[nx][ny]==1:
        g[nx][ny]=2
        q.append([nx, ny])
    tmp+=1
    d=direction(tmp)
    x, y = nx, ny
print(tmp)