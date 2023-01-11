import sys
input=sys.stdin.readline

def f(tmp):
    q=0
    if len(ans)==m:
        print(*ans)
    for i in range(n):
        if i not in tmp and arr[i]!=q:
            q=arr[i]
            ans.append(arr[i])
            tmp.append(i)
            f(tmp)
            ans.pop()
            tmp.pop()

n, m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
ans=[]
f([])