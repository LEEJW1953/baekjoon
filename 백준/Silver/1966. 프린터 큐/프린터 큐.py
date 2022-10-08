import sys
from collections import deque

t=int(sys.stdin.readline())
for i in range(t):
    n, m=map(int, sys.stdin.readline().split())
    arr=list(map(int, sys.stdin.readline().split()))
    q=deque()
    qq=deque(arr)
    for i in range(n):
        q.append([i, arr[i]])
    j=1
    while len(q)!=0:
        if q[0][1]==max(qq):
            if q[0][0]==m:
                print(j)
            q.popleft()
            qq.popleft()
            j+=1
        else:
            q.append(q.popleft())
            qq.append(qq.popleft())