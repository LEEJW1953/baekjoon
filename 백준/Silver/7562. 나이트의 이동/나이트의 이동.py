import sys
input=sys.stdin.readline
from collections import deque

def BFS():
    while True:
        temp=[]
        con=False
        while q:
            [x, y] = q.popleft()
            if x==x1 and y==y1:
                print(0)
                con=True
                break
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if nx==x1 and ny==y1:
                    print(arr[y][x])
                    q.clear()
                    con=True
                    break
                elif arr[ny][nx]==0:
                    arr[ny][nx]=arr[y][x]+1
                    temp.append([nx, ny])
        if temp:
            for i in range(len(temp)):
                q.append(temp[i])
        if con:
            break

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[[0]*n for _ in range(n)]
    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    q=deque()
    q.append([x, y])
    arr[y][x]=1
    dx=[-2, -1, 1, 2, -2, -1, 1, 2]
    dy=[1, 2, 2, 1, -1, -2, -2, -1]
    BFS()