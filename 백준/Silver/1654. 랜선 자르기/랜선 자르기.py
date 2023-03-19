import sys
input=sys.stdin.readline

def count(arr, a):
    result=0
    for i in range(k):
        result+=arr[i]//a
    return result

def bi(arr, start, end, nn):
    while start<=end:
        mid=(start+end)//2
        if count(arr, mid)>=nn:
            start=mid+1
        else:
            end=mid-1
    return end

k, n = map(int, input().split())
arr=[]
for i in range(k):
    arr.append(int(input()))
print(bi(arr, 1, max(arr), n))