import sys
input=sys.stdin.readline

ans=0
s=input().strip()
t=0
for i in range(len(s)):
    if s[i]=='(':
        t+=1
    else:
        t-=1
        if s[i-1]=='(':
            ans+=t
        else:
            ans+=1
print(ans)