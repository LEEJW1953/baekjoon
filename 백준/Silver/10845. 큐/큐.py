import sys
from collections import deque
n=int(sys.stdin.readline())
q=deque([])
for i in range(n):
    com=sys.stdin.readline().split()
    if com[0]=='push':
        q.append(com[1])
    if com[0]=='pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif com[0]=='size':
        print(len(q))
    elif com[0]=='empty':
        if not q:
            print(1)
        else:
            print(0)
    elif com[0]=='front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif com[0]=='back':
        if not q:
            print(-1)
        else:
            print(q[-1])