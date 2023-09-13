import sys
input=sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q=deque(range(1, n+1))
arr=[]
while q:
    q.rotate(-k+1)
    arr.append(str(q.popleft()))
print(f'<{", ".join(arr)}>')