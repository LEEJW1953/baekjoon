import sys
input=sys.stdin.readline

def f(x):
    global ans
    if len(arr)==2:
        ans=max(ans, x)
        return
    for i in range(1, len(arr)-1):
        tmp=arr[i]
        del arr[i]
        f(x+arr[i-1]*arr[i])
        arr.insert(i, tmp)

n=int(input())
arr=list(map(int, input().split()))
ans=0
f(0)
print(ans)