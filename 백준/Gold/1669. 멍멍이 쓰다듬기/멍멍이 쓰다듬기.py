import sys
input=sys.stdin.readline

x, y = map(int, input().split())
if x==y:
    print(0)
    exit(0)
diff=y-x
n = int(diff**0.5)
m = diff-n**2
ans=2*n-1
if m:
    ans+=1
    if m>n:
        ans+=1
print(ans)