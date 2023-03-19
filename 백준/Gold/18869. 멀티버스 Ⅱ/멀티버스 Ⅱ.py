import sys
input=sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
pair=defaultdict(int)
for _ in range(m):
    cosmos=list(map(int, input().split()))
    cosmos1=sorted(list(set(cosmos)))
    cosmos2={cosmos1[i]: i for i in range(len(cosmos1))}
    res=tuple(cosmos2[i] for i in cosmos)
    pair[res]+=1
val=pair.values()
answer=0
for i in val:
    answer+=i*(i-1)//2
print(answer)