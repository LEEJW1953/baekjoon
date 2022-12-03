import sys
input=sys.stdin.readline

n=int(input())
p=list(map(int, input().split()))
if n==1:
    print(p[0])
elif n==2:
    print(max(2*p[0], p[1]))
else:
    dp=[0, p[0], max(2*p[0], p[1])]
    for i in range(3, n+1):
        tmp=0
        dp.append(p[i-1])
        for j in range((i+2)//2):
            tmp=max(dp[j]+dp[len(dp)-j-1], tmp)
        dp[-1]=tmp
    print(dp[-1])