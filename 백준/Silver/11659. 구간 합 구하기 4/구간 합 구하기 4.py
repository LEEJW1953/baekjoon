import sys
input=sys.stdin.readline

n,m=map(int, input().split())
arr=list(map(int, input().split()))
sum=[0]
for i in range(len(arr)):
    sum.append(sum[i]+arr[i])
for _ in range(m):
    i,j=map(int, input().split())
    print(sum[j]-sum[i-1])