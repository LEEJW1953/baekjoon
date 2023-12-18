import sys
input=sys.stdin.readline

def f(x, y):
    res=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if g[nx][ny]=='.':
                res+=1
        else:
            res+=1
    return res>=3

r, c = map(int, input().split())
g=[list(input().strip()) for _ in range(r)]
ans=[['.']*c for i in range(r)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
top, bot, left, right = r, 0, c, 0
for i in range(r):
    for j in range(c):
        if g[i][j]=='X':
            if not f(i, j):
                ans[i][j]='X'
for i in range(r):
    for j in range(c):
        if ans[i][j]=='X':
            top=min(i, top)
            bot=max(i, bot)
            left=min(j, left)
            right=max(j, right)
for i in range(top, bot+1):
    print(''.join(ans[i][left:right+1]))