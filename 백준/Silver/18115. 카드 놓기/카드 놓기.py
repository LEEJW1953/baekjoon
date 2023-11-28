import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
arr=list(map(int, input().split()))
q=deque()
for i in range(len(arr)-1, -1, -1):
    if arr[i]==1:
        q.appendleft(n-i)
    elif arr[i]==2:
        tmp=q.popleft()
        q.appendleft(n-i)
        q.appendleft(tmp)
    else:
        q.append(n-i)
print(*q)