import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
d=defaultdict(int)
for _ in range(n):
    s=input().strip().split('.')
    d[s[1]]+=1
file=list(d.items())
file.sort(key=lambda x:x[0])
for i in range(len(file)):
    print(file[i][0], file[i][1])