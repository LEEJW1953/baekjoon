import sys
input=sys.stdin.readline
from collections import deque

def bfs(g,h,w):
    r=0
    vis=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j]=='#' and not vis[i][j]:
                q=deque()
                q.append([i, j])
                while q:
                    [x, y]=q.pop()
                    for k in range(4):
                        nx, ny=x+dx[k], y+dy[k]
                        if 0<=nx<h and 0<=ny<w:
                            if g[nx][ny]=='#' and not vis[nx][ny]:
                                q.append([nx, ny])
                                vis[nx][ny]=1
                r+=1
    return r


t=int(input())
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
for _ in range(t):
    h, w = map(int, input().split())
    g=[list((input().strip())) for _ in range(h)]
    print(bfs(g,h,w))