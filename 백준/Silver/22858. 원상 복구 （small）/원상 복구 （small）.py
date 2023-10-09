import sys
input=sys.stdin.readline

n, k = map(int, input().split())
s=list(map(int, input().split()))
d=list(map(int, input().split()))
ans=[0]*n
for j in range(k):
    for i in range(n):
        ans[d[i]-1]=s[i]
    s=ans[:]
print(*ans)