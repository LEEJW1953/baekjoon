import sys
input=sys.stdin.readline
from collections import deque

def bfs(x):
    q=deque()
    q.append(x)
    while q:
        nx=q.popleft()
        if nx==k:
            print(arr[k])
            exit(0)
        nx1=nx+1
        nx2=nx-1
        i=nx
        while i<=100001:
            if i==0:
                break
            if arr[nx]<arr[i] and not vis[i]:
                arr[i]=arr[nx]
                q.appendleft(i)
                vis[i]=1
            i*=2
        if 0<=nx1<100001:
            if arr[nx]+1<arr[nx1]:
                arr[nx1]=arr[nx]+1
                q.append(nx1)
        if 0<=nx2<100001:
            if arr[nx]+1<arr[nx2]:
                arr[nx2]=arr[nx]+1
                q.append(nx2)

n,k=map(int, input().split())
if k<=n:
    print(n-k)
else:
    arr=[int(1e9)]*100001
    vis=[0]*100001
    arr[n]=0
    bfs(n)