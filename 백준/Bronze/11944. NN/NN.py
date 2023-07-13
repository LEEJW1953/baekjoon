import sys
input=sys.stdin.readline

n, m = map(int, input().split())
s=''
for i in range(n):
    s+=str(n)
if len(s)>m:
    print(s[0:m])
else:
    print(s)