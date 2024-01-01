import sys
input=sys.stdin.readline

n=int(input())
ans=''
for i in range(n):
    s=input().strip()
    if not ans:
        ans=s
    tmp=''
    for j in range(len(ans)):
        if ans[j]!=s[j]:
            tmp+='?'
        else:
            tmp+=s[j]
    ans=tmp
print(ans)