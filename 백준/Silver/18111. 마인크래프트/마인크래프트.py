import sys
input=sys.stdin.readline

n, m, b = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
minn=300
maxx=0
total=b
for i in range(n):
    maxx=max(maxx, max(g[i]))
    minn=min(minn, min(g[i]))
    total+=sum(g[i])
t, h = 1e11, 0
for i in range(maxx, minn-1, -1):
    tmptime=0
    tmpheight=0
    for j in range(n):
        for k in range(m):
            if g[j][k]<i:
                tmptime+=i-g[j][k]
            elif g[j][k]>i:
                tmptime+=2*(g[j][k]-i)
    tmpheight=n*m*i
    if tmpheight<=total and tmptime<t:
        t=tmptime
        h=i
    elif tmptime==t and h<i:
        h=i
    if tmptime>t:
        break
print(t, h)