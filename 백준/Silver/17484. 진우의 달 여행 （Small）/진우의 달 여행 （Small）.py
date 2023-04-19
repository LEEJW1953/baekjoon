import sys
input=sys.stdin.readline

def dfs(x, y, d, total):
    global answer
    if answer<total:
        return
    if x==n-1:
        answer=min(answer, total)
        return
    for i in range(3):
        if i==d:
            continue
        elif 0<=y+dy[i]<m:
            dfs(x+1, y+dy[i], i, total+g[x+1][y+dy[i]])

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
answer=1e10
dy=[-1, 0, 1]
for i in range(m):
    dfs(0, i, -1, g[0][i])
print(answer)