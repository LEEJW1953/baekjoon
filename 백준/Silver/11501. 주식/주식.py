import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    m=arr[-1]
    sum=0
    for j in range(n-1, -1, -1):
        if arr[j]>m:
            m=arr[j]
        else:
            sum+=(m-arr[j])
    print(sum)