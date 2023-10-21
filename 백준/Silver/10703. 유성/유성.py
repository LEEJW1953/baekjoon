import sys
input=sys.stdin.readline

r, s = map(int, input().split())
g=[list(input().strip()) for _ in range(r)]
h=10000
for i in range(s):
    tmp=False
    dis=0
    for j in range(r):
        if g[j][i]=='X':
            tmp=True
            dis=0
        elif g[j][i]=='#' or j==r-1:
            if tmp:
                h=min(dis, h)
                break
        else:
            dis+=1
for i in range(r-1, -1, -1):
    for j in range(s):
        if g[i][j]=='X':
            g[i+h][j]='X'
            g[i][j]='.'
for i in range(r):
    sys.stdout.write(''.join(g[i]))
    sys.stdout.write('\n')