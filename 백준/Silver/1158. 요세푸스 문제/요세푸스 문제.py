import sys
input=sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q=deque(range(1, n+1))
arr=[]
for i in range(n):
    for j in range(k):
        q.append(q.popleft())
    arr.append(str(q.pop()))
print(f'<{", ".join(arr)}>')