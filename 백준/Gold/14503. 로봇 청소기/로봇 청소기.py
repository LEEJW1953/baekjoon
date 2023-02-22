import sys
input=sys.stdin.readline

def bfs():
    global count, r, c, d
    while True:
        tmp=False
        if not g[r][c]:
            g[r][c]=2
            count+=1
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<n and 0<=nc<m and not g[nr][nc]:
                tmp=True
        if tmp:
            d-=1
            if d<0:
                d+=4
            nr, nc = r+dx[d], c+dy[d]
            if 0<=nr<n and 0<=nc<m and not g[nr][nc]:
                r, c = nr, nc
        else:
            nd=d-2
            if nd<0:
                nd+=4
            nr, nc = r+dx[nd], c+dy[nd]
            if 0<=nr<n and 0<=nc<m:
                if g[nr][nc]==1:
                    return
                r, c = nr, nc

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count=0
n, m = map(int, input().split())
r, c, d = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
bfs()
print(count)