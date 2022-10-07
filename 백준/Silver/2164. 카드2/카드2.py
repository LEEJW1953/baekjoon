import sys
from collections import deque

n=int(sys.stdin.readline())
q=deque()
for i in range(n):
    q.append(i+1)
if len(q)==1:
    print(1)
else:
    while len(q)!=1:
        q.popleft()
        a = q.popleft()
        q.append(a)
    print(a)