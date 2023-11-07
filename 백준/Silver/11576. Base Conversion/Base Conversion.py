import sys
input=sys.stdin.readline

def sol(n, q):
    res=[]
    while n>0:
        n, mod = divmod(n, q)
        res.append(mod)
    return res[::-1]

a, b = map(int, input().split())
m=int(input())
arr=list(map(int, input().split()))
res=0
for i in range(m):
    res+=arr[i]*a**(m-1-i)
print(*sol(res, b))