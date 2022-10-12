import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
for i in range(t):
    p=input().rstrip()
    n=int(input())
    result=0
    q=deque(input().rstrip()[1:-1].split(','))
    if n==0:
        q=deque()
    rcount=0
    for i in p:
        if i=='R':
            rcount+=1
        elif i=='D':
            if len(q)==0:
                print('error')
                result=1
                break
            else:
                if rcount%2==1:
                    q.pop()
                else:
                    q.popleft()
    if result==0:
        if rcount%2==1:
            q.reverse()
        print("[" + ",".join(q) + "]")