import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
d=defaultdict(int)
ans=0
for _ in range(n):
    s=input().strip()
    if s=='ENTER':
        tmp=False
        arr=list(d.values())
        ans+=sum(arr)
        d=defaultdict(int)
    else:
        tmp=True
        if d[s]:
            continue
        else:
            d[s]=1
if tmp:
    arr=list(d.values())
    ans+=sum(arr)
print(ans)