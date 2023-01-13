import sys
input=sys.stdin.readline

def f():
    if len(s)==m:
        # print(*s)
        ans.add(' '.join(map(str, s)))
        return
    for i in range(n):
        s.append(arr[i])
        f()
        s.pop()

n, m=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
s=[]
ans=set()
f()
ans=list(ans)
res=[]
for i in range(len(ans)):
    res.append(list(map(int, ans[i].split())))
res.sort()
for i in range(len(res)):
    print(*res[i])