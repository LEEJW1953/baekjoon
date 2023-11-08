import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    m, n = map(int, input().split())
    g=[list(map(int, input().split())) for _ in range(m)]
    ans=0
    for i in range(n):
        for j in range(m-1, -1, -1):
            if g[j][i]:
                count=0
                for k in range(m-1, j-1, -1):
                    if not g[k][i]:
                        count+=1
                ans+=count
    print(ans)
