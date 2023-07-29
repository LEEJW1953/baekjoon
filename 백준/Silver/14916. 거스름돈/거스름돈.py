import sys
input=sys.stdin.readline

n=int(input())
dp=[0, -1, 1, -1, 2, 1]
for i in range(6, 100001):
    a=dp[i-5]
    b=dp[i-2]
    if a!=-1 and b!=-1:
        dp.append(min(a, b)+1)
    else:
        if a!=-1:
            dp.append(a+1)
        elif b!=-1:
            dp.append(b+1)
        else:
            dp.append(-1)
print(dp[n])