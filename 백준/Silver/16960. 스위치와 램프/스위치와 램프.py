import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr=[]
d={}
for i in range(n):
    tmp=list(map(int, input().split()))
    arr.append(tmp[1:])
    for j in tmp[1:]:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
for tmp in arr:
    q=d.copy()
    for i in tmp:
        if i not in q:
            q[i]=d[i]=1
        else:
            q[i]-=1
    res=list(q.values())
    if 0 not in res:
        print(1)
        exit(0)
print(0)