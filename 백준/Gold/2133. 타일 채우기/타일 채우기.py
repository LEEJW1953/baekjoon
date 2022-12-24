n=int(input())
if n%2==1:
    print(0)
else:
    dp=[0]*(n//2+1)
    dp[1]=3
    for i in range(2, n//2+1):
        dp[i]+=3*dp[i-1]+2
        for j in range(2, i):
            dp[i]+=2*dp[i-j]
    print(dp[-1])