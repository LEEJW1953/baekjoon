import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(n)]
    ans1=[0]*n
    ans2=[0]*n
    for i in range(n):
        for j in range(n):
            ans1[i]+=arr[i][j]
            ans2[i]+=arr[j][i]
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1-1, r2):
            ans1[i]+=(c2-c1+1)*v
        for i in range(c1-1, c2):
            ans2[i]+=(r2-r1+1)*v
    print(*ans1)
    print(*ans2)