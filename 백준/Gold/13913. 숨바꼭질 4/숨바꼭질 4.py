import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x+1<100001 and not arr[x+1]:
            arr[x+1]=[arr[x][0]+1, x]
            q.append(x+1)
        if x-1>=0 and not arr[x-1]:
            arr[x-1]=[arr[x][0]+1, x]
            q.append(x-1)
        if 2*x<100001 and not arr[2*x]:
            arr[2*x]=[arr[x][0]+1, x]
            q.append(2*x)


arr=[[]]*100002
n, k=map(int, input().split())
res=[k]
arr[n]=[0, 0]
bfs()
tmp=k
for i in range(arr[k][0]):
    res.append(arr[tmp][1])
    tmp=arr[tmp][1]
res.reverse()
print(arr[k][0])
print(*res)