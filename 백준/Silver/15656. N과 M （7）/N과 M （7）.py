import sys
input=sys.stdin.readline

def f():
    if len(ans)==m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        ans.append(arr[i])
        f()
        ans.pop()

n, m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
ans=[]
f()