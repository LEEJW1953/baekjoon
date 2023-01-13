import sys
input=sys.stdin.readline

def f(x):
    q=0
    if len(s)==m:
        print(*s)
        return
    for i in range(x, n):
        if arr[i]!=q:
            s.append(arr[i])
            q=arr[i]
            f(i)
            s.pop()

n, m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
s=[]
f(0)