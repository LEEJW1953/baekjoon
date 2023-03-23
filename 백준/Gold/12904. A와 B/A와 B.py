import sys
input=sys.stdin.readline

s=input().strip()
t=input().strip()
for i in range(len(t)-len(s)):
    if t[-1]=='A':
        t=t[0:-1]
    elif t[-1]=='B':
        t=t[0:-1][::-1]
if t==s:
    print(1)
else:
    print(0)