import sys
input=sys.stdin.readline
def count(t):
    if g[i][j]=='J':
        t[0]+=1
    if g[i][j]=='O':
        t[1]+=1
    if g[i][j]=='I':
        t[2]+=1
    return t
m,n=map(int, input().split())
k=int(input())
g=[list(input().strip()) for _ in range(m)]
s=[[[0,0,0] for _ in range(n+1)]]
for i in range(m):
    t=[[0,0,0]]
    for j in range(n):
        c=count(t[j][:])
        c[0]+=s[i][j+1][0]-s[i][j][0]
        c[1]+=s[i][j+1][1]-s[i][j][1]
        c[2]+=s[i][j+1][2]-s[i][j][2]
        t.append(c)
    s.append(t)
for _ in range(k):
    a,b,c,d=map(int, input().split())
    [j,o,i]=[s[c][d][i]-s[c][b-1][i]-s[a-1][d][i]+s[a-1][b-1][i] for i in range(3)]
    print(j,o,i)