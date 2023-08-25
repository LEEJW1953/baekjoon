import sys
input=sys.stdin.readline

a, b, c, m = map(int, input().split())
t, ans = 0, 0
for i in range(24):
    if t+a<=m:
        ans+=b
        t+=a
    else:
        t-=c
        if t<0:
            t=0
print(ans)