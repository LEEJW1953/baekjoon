import sys
input=sys.stdin.readline
from itertools import permutations

def f(arr, t, order):
    x, y = xs, ys
    tmp=0
    for i in range(3):
        if order[i]==1:
            tmp+=abs(arr[t[i]][0]-x)
            tmp+=abs(arr[t[i]][1]-y)
            tmp+=10
            x=arr[t[i]][2]
            y=arr[t[i]][3]
        if order[i]==2:
            tmp+=abs(arr[t[i]][2]-x)
            tmp+=abs(arr[t[i]][3]-y)
            tmp+=10
            x=arr[t[i]][0]
            y=arr[t[i]][1]
    tmp+=abs(x-xe)
    tmp+=abs(y-ye)
    return tmp

xs, ys = map(int,input().split())
xe, ye = map(int,input().split())
arr=[]
INF=1e12
ans=INF
for i in range(3):
    arr.append(list(map(int,input().split())))
for t in permutations(range(3), 3):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                order=[i, j, k]
                ans=min(ans, f(arr, t, order))
print(ans)