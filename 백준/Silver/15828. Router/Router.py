import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
q=deque()
while True:
    r=int(input())
    if r==-1:
        break
    if r==0:
        q.popleft()
    elif len(q)==n:
        continue
    else:
        q.append(r)
if q:
    for i in range(len(q)):
        print(q[i], end=' ')
else:
    print("empty")