import sys
input=sys.stdin.readline

n, q = map(int, input().split())
d={}
for i in range(q):
    goal=int(input())
    loc=goal
    parent=[loc]
    i=0
    go=True
    while loc>1:
        tmp=loc%2
        if tmp:
            loc-=1
        loc//=2
        parent.append(loc)
    parent.sort()
    for node in parent:
        if node in d:
            print(node)
            go=False
            break
    if go:
        print(0)
        d[goal]=1