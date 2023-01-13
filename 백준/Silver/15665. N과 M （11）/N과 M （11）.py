import sys
input=sys.stdin.readline

def f():
    q=0
    if len(s)==m:
        print(*s)
        return
    for i in range(n):
        if arr[i]!=q:
            s.append(arr[i])
            q=arr[i]
            f()
            s.pop()

n, m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
s=[]
f()