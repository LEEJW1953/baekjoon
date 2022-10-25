import sys
input=sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
arr=[[0], [1]]
for i in range(2, n+1):
    a=dp[i-1]+1
    if i % 2 == 0:
        b=dp[i//2]+1
    else:
        b=999
    if i % 3 == 0:
        c=dp[i//3]+1
    else:
        c=999
    dp[i]=min(a, b, c)
    if dp[i]==c:
        arr1=arr[i//3].copy()
        arr1.append(i)
        arr.append(arr1)
    elif dp[i]==b:
        arr1=arr[i//2].copy()
        arr1.append(i)
        arr.append(arr1)
    elif dp[i]==a:
        arr1=arr[i-1].copy()
        arr1.append(i)
        arr.append(arr1)
print(dp[n])
for i in range(len(arr[n])):
    print(arr[n][-1-i], end=' ')