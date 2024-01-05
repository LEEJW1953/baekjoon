import sys
input=sys.stdin.readline

n, m = map(int, input().split())
if not n:
    print(0)
else:
    arr=list(map(int, input().split()))
    ans=1
    w=0
    for i in range(n):
        if w+arr[i]<=m:
            w+=arr[i]
        else:
            ans+=1
            w=arr[i]
    print(ans)