import sys
input=sys.stdin.readline
from collections import deque

def move(x, y, dx, dy):
    tmp=0
    while g[x+dx][y+dy]!="#" and g[x][y]!="O":
        x+=dx
        y+=dy
        tmp+=1
    return x, y, tmp

def bfs(start):
    q=deque()
    q.append(start)
    vis=[]
    vis.append([start[0], start[1], start[2], start[3]])
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count>10:
            break
        for i in range(4):
            nrx, nry, mr = move(rx, ry, dx[i], dy[i])
            nbx, nby, mb = move(bx, by, dx[i], dy[i])
            if g[nbx][nby]!="O":
                if g[nrx][nry]=="O":
                    print(count)
                    return
                if nrx==nbx and nry==nby:
                    if mr<mb:
                        nbx-=dx[i]
                        nby-=dy[i]
                    else:
                        nrx-=dx[i]
                        nry-=dy[i]
                if [nrx, nry, nbx, nby] not in vis:
                    vis.append([nrx, nry, nbx, nby])
                    q.append([nrx, nry, nbx, nby, count+1])
    print(-1)
    return


n, m = map(int, input().split())
g=[list(map(str, input().strip())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j]=="B":
            bx, by = i, j
        if g[i][j]=="R":
            rx, ry = i, j
start=[rx, ry, bx, by, 1]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
bfs(start)