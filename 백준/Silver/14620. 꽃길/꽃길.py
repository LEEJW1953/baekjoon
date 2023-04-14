import sys
input=sys.stdin.readline

def pick(x, y):
    if len(seed)==3:
        price(seed)
        return
    for i in range(1, n-1):
        for j in range(1, n-1):
            seed.append([i, j])
            pick(i, j)
            seed.pop()

def price(arr):
    global total
    p=0
    vis=[[0]*n for _ in range(n)]
    for s in arr:
        x, y = s[0], s[1]
        if vis[x][y] or total<p:
            return
        p+=g[x][y]
        vis[x][y]=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if vis[nx][ny] or total<p:
                return
            p+=g[nx][ny]
            vis[nx][ny]=1
    total=min(total, p)
    return

n=int(input())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
seed=[]
total = int(1e11)
for i in range(1, n-1):
    for j in  range(1, n-1):
        seed.append([i, j])
        pick(i, j)
        seed.pop()
print(total)