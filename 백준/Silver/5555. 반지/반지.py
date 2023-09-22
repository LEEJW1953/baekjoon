import sys
input=sys.stdin.readline

def f(x):
    return True

s=input().strip()
n=int(input())
ans=0
for i in range(n):
    t=input().strip()
    t+=t
    for j in range(10):
        if t[j:j+len(s)]==s:
            ans+=1
            break
print(ans)