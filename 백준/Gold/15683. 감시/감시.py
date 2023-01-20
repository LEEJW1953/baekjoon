import sys
input=sys.stdin.readline
from copy import deepcopy

def f(x):
    if len(s)==len(cctv):
        watch(cctv, s)
        return
    for i in range(cctv[x][3]):
        s.append(i)
        f(x+1)
        s.pop()

def watch(camera, arr):
    global answer
    gg=deepcopy(g)
    count=0
    for i in range(len(camera)):
        x, y=camera[i][0], camera[i][1]
        cctv=camera[i][2]
        delta=move[cctv]
        for j in delta[arr[i]]:
            nx, ny=x, y
            while 0<=nx<m and 0<=ny<n:
                if gg[ny][nx]==0:
                    gg[ny][nx]='#'
                if gg[ny][nx]==6:
                    break
                nx+=j[0]
                ny+=j[1]
    
    for i in range(n):
        for j in range(m):
            if gg[i][j]==0:
                count+=1
    answer=min(answer, count)
    return


n, m=map(int, input().split())
g=[]
cctv=[]
s=[]
move=[
    [[[1, 0]], [[0, 1]], [[-1, 0]], [[0, -1]]],
    [[[1, 0], [-1, 0]], [[0, -1], [0, 1]]],
    [[[0, -1], [1, 0]], [[1, 0], [0, 1]], [[0, 1], [-1, 0]], [[-1, 0], [0, -1]]],
    [[[-1, 0], [0, -1], [1, 0]], [[0, -1], [1, 0], [0, 1]], [[1, 0], [0, 1], [-1, 0]], [[0, 1], [-1, 0], [0, -1]]],
    [[[1, 0], [0, 1], [-1, 0], [0, -1]]]
]
answer=100
for i in range(n):
    g.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if g[i][j]!=0 and g[i][j]!=6:
            if g[i][j]==5:
                tmp=1
            elif g[i][j]==2:
                tmp=2
            else:
                tmp=4
            cctv.append([j, i, g[i][j]-1, tmp])
f(0)
print(answer)