import sys
input=sys.stdin.readline
from itertools import combinations

def f(count):
    global answer
    for i in combinations(range(n), count):
        tmp=[]
        for j in i:
            tmp.append(arr[j])
        if l<=sum(tmp)<=r and x<=max(tmp)-min(tmp):
            answer+=1
    return

n, l, r, x = map(int, input().split())
arr=list(map(int, input().split()))
answer=0
for i in range(2, n+1):
    f(i)
print(answer)