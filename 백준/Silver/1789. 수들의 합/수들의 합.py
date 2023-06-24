import sys
input=sys.stdin.readline

s=int(input())
ans=0
i=1
while i<=s:
    ans+=1
    s-=i
    i+=1
print(ans)