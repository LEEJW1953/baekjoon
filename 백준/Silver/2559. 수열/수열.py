import sys
input=sys.stdin.readline

n, k=map(int, input().split())
arr=list(map(int, input().split()))
sum=[0]
arr1=[]
for i in range(len(arr)):
    sum.append(sum[i]+arr[i])
for i in range(n-k+1):
    arr1.append(sum[i+k]-sum[i])
print(max(arr1))