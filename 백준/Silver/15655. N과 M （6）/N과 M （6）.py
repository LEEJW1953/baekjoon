import sys
input=sys.stdin.readline

def f(x):
    if len(ans)==m:
        print(' '.join(map(str, ans)))
        return
    for i in range(x, n):
        ans.append(arr[i])
        f(i+1)
        ans.pop()

n, m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
ans=[]
f(0)