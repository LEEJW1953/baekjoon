n=int(input())
dp=[1, 1]
for i in range(82):
    dp.append(dp[i]+dp[i+1])
print(2*(dp[n]+dp[n-1]))