import sys
input=sys.stdin.readline

n=int(input())
s=input().strip()
r, b = 0, 0
if s[0]=='R':
    r+=1
else:
    b+=1
for i in range(1, n):
    if s[i]!=s[i-1]:
        if s[i]=='R':
            r+=1
        else:
            b+=1
print(min(r, b)+1)