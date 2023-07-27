import sys
input=sys.stdin.readline
from collections import defaultdict

s1, s2, s3 = map(int, input().split())
d=defaultdict(int)
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            t=i+j+k
            d[t]+=1
arr=list(d.items())
arr.sort(key=lambda x:(-x[1], x[0]))
print(arr[0][0])