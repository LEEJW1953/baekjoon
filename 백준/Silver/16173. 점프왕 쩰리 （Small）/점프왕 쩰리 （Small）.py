import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append([0, 0])
    vis[0][0]=1
    while q:
        [xx, yy]=q.popleft()
        if g[xx][yy]==-1:
            print('HaruHaru')
            exit(0)
        for i in range(2):
            nx, ny = xx+dx[i]*g[xx][yy], yy+dy[i]*g[xx][yy]
            if 0<=nx<n and 0<=ny<n:
                if not vis[nx][ny]:
                    q.append([nx, ny])
                    vis[nx][ny]=1
    print('Hing')
    return

n=int(input())
g=[list(map(int, input().split())) for _ in range(n)]
vis=[[0]*n for _ in range(n)]
dx=[1, 0]
dy=[0, 1]
bfs()