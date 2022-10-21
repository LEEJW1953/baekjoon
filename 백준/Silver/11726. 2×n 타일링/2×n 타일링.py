import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*1001
arr[1]=1
arr[2]=2
arr[3]=3
if n>=4:
    for i in range(4, n+1):
        arr[i]=(arr[i-1]+arr[i-2])%10007
print(arr[n])