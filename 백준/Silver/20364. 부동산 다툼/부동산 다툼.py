import sys
input=sys.stdin.readline

n, q = map(int, input().split())
d={}
for i in range(q):
    goal=int(input())
    loc=goal
    block=0
    while loc>1:
        if loc in d:
            block=loc
        loc//=2
    if not block:
        d[goal]=1
    print(block)