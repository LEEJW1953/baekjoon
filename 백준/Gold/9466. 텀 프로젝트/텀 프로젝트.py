import sys
input=sys.stdin.readline

sys.setrecursionlimit(111111)

def DFS(x):
    global res
    vis[x]=True
    cycle.append(x)
    num=arr[x]

    if vis[num]:
        if num in cycle:
            res+=cycle[cycle.index(num):]
        return
    else:
        DFS(num)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[0]+list(map(int, input().split()))
    vis=[False]*(n+1)
    res=[]
    for i in range(1, n+1):
        if not vis[i]:
            cycle=[]
            DFS(i)
    print(n-len(res))