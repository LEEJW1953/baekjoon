import sys
input=sys.stdin.readline

n=int(input())
s=input().strip()
c1, c2 = 0, 0
for i in range(n-1, -1, -1):
    tmp=s[i]
    if tmp=='s':
        c1+=1
    else:
        c2+=1
    if c1==c2:
        ans=i
print(s[ans:])