import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy
from itertools import permutations, product

def rotate(board):
    arr=[[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            arr[4-j][i]=board[i][j]
    return arr

def route():
    for i in product([0, 1, 2, 3], repeat=5):
        for j in permutations([0, 1, 2, 3, 4], 5):
            bfs(j, i)

def bfs(order, direction):
    global result
    maze_now=deepcopy(maze)
    newmaze=[]
    for i in order:
        for _ in range(direction[i]+1):
            maze_now[i]=rotate(maze_now[i])
        newmaze.append(maze_now[i])
    if not newmaze[0][0][0] or not newmaze[4][4][4]:
        return
    vis=[[[-1]*5 for _ in range(5)] for _ in range(5)]
    q=deque()
    q.append([0, 0, 0])
    vis[0][0][0]=0
    while q:
        [xx, yy, zz] = q.popleft()
        if xx==4 and yy==4 and zz==4:
            if vis[4][4][4]==12:
                print(12)
                exit(0)
            result=min(result, vis[4][4][4])
            break
        for j in range(6):
            nx=xx+dx[j]
            ny=yy+dy[j]
            nz=zz+dz[j]
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                if newmaze[nx][ny][nz]==1 and vis[nx][ny][nz]==-1:
                    vis[nx][ny][nz]=vis[xx][yy][zz]+1
                    q.append([nx, ny, nz])
    return

result=100000
dx=[1, -1, 0, 0, 0, 0]
dy=[0 ,0, 1, -1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]
maze=[[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
route()
if result<1000:
    print(result)
else:
    print(-1)