import sys
input=sys.stdin.readline

def check(x):
    if x==0:
        return True
    count=0
    for i in range(n):
        count+=arr[i]//x
        if k<=count:
            return True
    return k<=count

def search():
    left, right = 0, max(arr)
    tmp=(left+right)//2
    while left<=right:
        mid=(left+right)//2
        if check(mid):
            tmp=mid
            left=mid+1
        else:
            tmp=mid-1
            right=mid-1
    return tmp

n, k = map(int, input().split())
arr=[int(input()) for _ in range(n)]
print(search())