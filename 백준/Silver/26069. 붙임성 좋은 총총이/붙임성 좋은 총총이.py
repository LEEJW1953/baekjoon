import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
vis=defaultdict(int)
for _ in range(n):
    a, b = input().split()
    if a=='ChongChong':
        vis[a]=1
    if b=='ChongChong':
        vis[b]=1
    if vis[a]:
        vis[b]=1
    if vis[b]:
        vis[a]=1
print(sum(vis.values()))