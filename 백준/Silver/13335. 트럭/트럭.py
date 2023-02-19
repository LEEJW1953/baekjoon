import sys
input=sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())
t=deque(map(int, input().split()))
arr=[0]*w
result=0
total=0
while t or arr:
    if t:
        tmp=t.popleft()
        total-=arr.pop()
        if (total+tmp)<=l:
            arr.insert(0, tmp)
            total+=tmp
        else:
            arr.insert(0, 0)
            t.appendleft(tmp)
        result+=1
    else:
        while arr:
            tmp=arr.pop()
            if tmp:
                total-=tmp
            result+=1
print(result)