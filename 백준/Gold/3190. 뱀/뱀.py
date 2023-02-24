import sys
input=sys.stdin.readline
from collections import deque

def direction(d, time):
    if move[time]=="L":
        d=(d-1)%4
    elif move[time]=="D":
        d=(d+1)%4
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
move = {}
for _ in range(l):
    xx, dd = map(str, input().split())
    xx=int(xx)
    move[xx]=dd
tmp=0
while True:
    nx, ny = x+dx[d], y+dy[d]
    tmp+=1
    if nx<0 or ny<0 or n<=nx or n<=ny or g[nx][ny]==2:
        break
    if g[nx][ny]==0:
        g[nx][ny]=2
        q.append([nx, ny])
        end=q.popleft()
        g[end[0]][end[1]]=0
    elif g[nx][ny]==1:
        g[nx][ny]=2
        q.append([nx, ny])
    if tmp in move:
        d=direction(d, tmp)
    x, y = nx, ny
print(tmp)