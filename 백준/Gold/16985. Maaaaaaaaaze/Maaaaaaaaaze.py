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
    for i in range(len(direction)):
        for j in range(len(order)):
            bfs(order[j], direction[i])

def bfs(order, direction):
    global result
    maze_now=deepcopy(maze)
    newmaze=[]
    for i in order:
        for _ in range(direction[i]+1):
            maze_now[i]=rotate(maze_now[i])
        newmaze.append(maze_now[i])
    stx, sty, stz = 0, 0, 0
    enx, eny, enz = 4, 4, 4
    if not newmaze[stx][sty][stz] or not newmaze[enx][eny][enz]:
        return
    newmaze1=deepcopy(newmaze)
    q=deque()
    q.append([stx, sty, stz])
    while q:
        [xx, yy, zz] = q.popleft()
        if xx==enx and yy==eny and zz==enz:
            result=min(result, newmaze1[enx][eny][enz])
            if result==13:
                print(12)
                exit(0)
            break
        for j in range(6):
            nx=xx+dx[j]
            ny=yy+dy[j]
            nz=zz+dz[j]
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                if newmaze1[nx][ny][nz]==1:
                    newmaze1[nx][ny][nz]=newmaze1[xx][yy][zz]+1
                    q.append([nx, ny, nz])
    return

result=100000
maze=[]
order=[]
direction=[]
dx=[1, -1, 0, 0, 0, 0]
dy=[0 ,0, 1, -1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]
st=[[0, 0, 0], [0, 0, 4], [0, 4, 0], [0, 4, 4]]
en=[[4, 4, 4], [4, 4, 0], [4, 0, 4], [4, 0, 0]]
order=list(permutations([0, 1, 2, 3, 4], 5))
direction=list(product([0, 1, 2, 3], repeat=5))
for i in range(5):
    arr=[]
    for j in range(5):
        arr.append(list(map(int, input().split())))
    maze.append(arr)
route()
if result<1000:
    print(result-1)
else:
    print(-1)