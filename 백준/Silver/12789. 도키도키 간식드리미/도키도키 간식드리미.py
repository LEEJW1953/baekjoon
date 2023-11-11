import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
q=deque(map(int, input().split()))
s=deque()
for i in range(1, n+1):
    if s:
        tmp=s.pop()
        if tmp==i:
            continue
        else:
            s.append(tmp)
    while True:
        if not q:
            print('Sad')
            exit(0)
        tmp1=q.popleft()
        if tmp1==i:
            break
        s.append(tmp1)
print('Nice')