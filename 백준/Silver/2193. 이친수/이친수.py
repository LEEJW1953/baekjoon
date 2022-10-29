import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*91
arr[1]=1
arr[2]=1
arr[3]=2
for i in range(4, n+1):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[n])