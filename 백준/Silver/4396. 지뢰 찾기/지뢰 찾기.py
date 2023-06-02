import sys
input=sys.stdin.readline

def open(x, y):
    global bomb
    result=0
    if g[x][y]=='*':
        bomb=True
        return '*'
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if g[nx][ny]=='*':
                result+=1
    return result

n=int(input())
g=[list(input().strip()) for _ in range(n)]
arr=[list(input().strip()) for _ in range(n)]
dx=[-1, -1, -1, 0, 0, 1, 1, 1]
dy=[-1, 0, 1, -1, 1, -1, 0, 1]
ans=[]
bomb=False
for i in range(n):
    tmp=[]
    for j in range(n):
        if arr[i][j]=='x':
            tmp.append(str(open(i, j)))
        else:
            tmp.append('.')
    ans.append(tmp)
if bomb:
    for i in range(n):
        for j in range(n):
            if g[i][j]=='*':
                ans[i][j]='*'
for i in range(n):
    print(''.join(ans[i]))