import sys
input=sys.stdin.readline

n=int(input())
dp=[1, 2, 7]
total=0
for i in range(3, 1000001):
    total+=dp[i-3]
    dp.append((dp[i-2]*3+dp[i-1]*2+2*total)%1000000007)
print(dp[n])