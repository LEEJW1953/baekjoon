import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    arr.sort()
    res=[0]*n
    ans=0
    for i in range(n):
        if i%2:
            res[n-1-i//2]=arr[i]
        else:
            res[i//2]=arr[i]
    for i in range(n):
        if i==n-1:
            ans=max(ans, abs(res[i]-res[0]))
        else:
            ans=max(ans, abs(res[i+1]-res[i]))
    print(ans)