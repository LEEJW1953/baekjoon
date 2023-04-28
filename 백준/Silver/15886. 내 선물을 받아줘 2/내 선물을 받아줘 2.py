import sys
input=sys.stdin.readline

n=int(input())
s=input().strip()
ans=0
for i in range(n-1):
    if s[i:i+2]=='EW':
        ans+=1
print(ans)