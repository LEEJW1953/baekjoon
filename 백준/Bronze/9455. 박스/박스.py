import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    m, n = map(int, input().split())
    g=[list(map(int, input().split())) for _ in range(m)]
    ans=0
    for i in range(n):
        count=0
        for j in range(m):
            if g[j][i]:
                count+=1
            else:
                ans+=count
    print(ans)