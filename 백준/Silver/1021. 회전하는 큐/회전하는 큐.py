import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
q=deque()
for i in range(n):
    q.append(i+1)
arr=list(map(int, input().split()))
result=0
for i in range(len(arr)):
    q1=q.copy()
    count1=0
    count2=0
    while q[0]!=arr[i]and q1[0]!=arr[i]:
        q.rotate(1)
        q1.rotate(-1)
        count1+=1
        count2+=1
    if q[0]==arr[i]:
        q.popleft()
    elif q1[0]==arr[i]:
        q1.popleft()
        q=q1
    result+=min(count1, count2)
print(result)