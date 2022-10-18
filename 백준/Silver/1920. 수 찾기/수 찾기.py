import sys
input=sys.stdin.readline

def fun(a):
    start=0
    end=n-1
    result=0
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==a:
            result=1
            return result
        if arr[mid]<a:
            start=mid+1
        elif a<arr[mid]:
            end=mid-1
    return result

n=int(input())
arr=list(map(int, input().split()))
arr.sort()
m=int(input())
arr1=list(map(int, input().split()))
for i in range(m):
    print(fun(arr1[i]))