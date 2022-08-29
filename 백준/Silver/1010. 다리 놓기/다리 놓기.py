import sys
input=sys.stdin.readline

t=int(input())
for a in range(t):
    m, n=map(int, input().split())
    arr=[[0]*(n+1) for i in range(n+1)]
    arr[0][0:(n+1)]=[1]*(n+1)
    for i in range(n+1):
        arr[i][0]=1
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j]=arr[i-1][j]+arr[i][j-1]
    print((arr[n-m][m]))