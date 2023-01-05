import sys
input=sys.stdin.readline

n=int(input())
dp=[1e9]*(n+1)
for i in range(1, n+1):
    if i**0.5==int(i**0.5):
        dp[i]=1
    else:
        num=int(i**0.5)
        for j in range(num//2, num+1):
            dp[i]=min(dp[i], dp[j**2]+dp[i-j**2])
print(dp[n])