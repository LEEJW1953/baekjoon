import sys
input=sys.stdin.readline

n=int(input())
s=input().strip()
count=1
ans=0
for i in range(len(s)-1):
    if abs(ord(s[i])-ord(s[i+1]))==1:
        count+=1
    else:
        ans=max(ans, count)
        count=1
ans=max(ans, count)
if ans>=5:
    print('YES')
else:
    print('NO')