import sys
input=sys.stdin.readline

def count(arr, a):
    result=0
    for i in range(n):
        res=arr[i]-a
        if res<0:
            res=0
        result+=res
    return result

def bi(arr, start, end, nn):
    while start<=end:
        mid=(start+end)//2
        if count(arr, mid)>=nn:
            start=mid+1
        else:
            end=mid-1
    return end

n, m = map(int, input().split())
arr=list(map(int, input().split()))
print(bi(arr, 0, max(arr), m))