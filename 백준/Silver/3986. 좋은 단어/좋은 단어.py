import sys
input=sys.stdin.readline
from collections import deque

def f(num, s):
    q=deque()
    for i in s:
        if q:
            a=q.pop()
            if i==a:
                continue
            else:
                q.append(a)
                q.append(i)
        else:
            q.append(i)
    if not q:
        return True
    else:
        return False

n=int(input())
arr=[]
count=0
for i in range(n):
    arr.append(input().strip())
for i in range(n):
    if f(i, arr[i]):
        count+=1
print(count)