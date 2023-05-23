import sys
input=sys.stdin.readline
from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    d=defaultdict(int)
    for i in range(n):
        arr=list(map(int, input().split()))
        for j in range(m):
            d[arr[j]]+=1
    res=list(d.items())
    res.sort(key=lambda x:(-x[1], x[0]))
    maxx=(list(set(d.values()))[-2])
    ans=[]
    for i in range(len(res)):
        if res[i][1]==maxx:
            ans.append(res[i][0])
    print(' '.join(list(map(str, ans))))