import sys
input=sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
cow=sorted(list(map(int, input().split())))
ans=set()

arr=[1]*(1000*m+1)
arr[0]=arr[1]=0
for i in range(int(len(arr)**0.5)+1):
    if arr[i]:
        for j in range(2*i, len(arr), i):
            arr[j]=0

for j in combinations(range(n), m):
    total=0
    for k in j:
        total+=cow[k]
    if arr[total]:
        ans.add(total)
ans=list(ans)
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)