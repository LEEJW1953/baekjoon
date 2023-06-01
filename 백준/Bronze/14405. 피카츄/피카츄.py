import sys
input=sys.stdin.readline

s=input().strip()
tmp=True
while s and tmp:
    s1=s[:2]
    s2=s[:3]
    if s1=='pi' or s1=='ka':
        s=s[2:]
    elif s2=='chu':
        s=s[3:]
    else:
        tmp=False
if tmp:
    print('YES')
else:
    print('NO')