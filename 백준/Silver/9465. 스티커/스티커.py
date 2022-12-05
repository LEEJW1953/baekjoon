import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    arr=[]
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    if n==1:
        print(max(arr[0][0], arr[1][0]))
    else:
        dp=[[arr[0][0], arr[1][0]], [arr[1][0]+arr[0][1], arr[0][0]+arr[1][1]]]
        for j in range(2, n):
            arr1=[]
            arr1.append(max(dp[j-2][1], dp[j-1][1])+arr[0][j])
            arr1.append(max(dp[j-2][0], dp[j-1][0])+arr[1][j])
            dp.append(arr1)
        print(max(dp[-1]))