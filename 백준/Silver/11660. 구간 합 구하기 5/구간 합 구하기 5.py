from re import A
import sys

n, m = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr1=[[0]*1025 for _ in range(1025)]
for i in range(1, n+1):
    dp=[arr[i-1][0]]
    for j in range(1, n):
        dp.append(dp[-1]+arr[i-1][j])
    for j in range(1, n+1):
        arr1[i][j]=arr1[i-1][j]+dp[j-1]
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(arr1[x2][y2]-arr1[x1-1][y2]-arr1[x2][y1-1]+arr1[x1-1][y1-1])