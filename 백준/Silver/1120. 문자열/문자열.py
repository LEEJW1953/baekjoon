import sys
input=sys.stdin.readline

a, b = map(str, input().split())
answer=1e9
n, m = len(a), len(b)
for i in range(m-n+1):
    tmp=0
    s=b[i:i+n]
    for j in range(n):
        if s[j]!=a[j]:
            tmp+=1
    answer=min(answer, tmp)
print(answer)