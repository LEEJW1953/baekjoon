import sys
input=sys.stdin.readline

n=int(input())
s=input().strip()
c1, c2 = 0, 0
for i in s:
    if i=='A':
        c1+=1
    else:
        c2+=1
if c1==c2:
    print('Tie')
elif c1>c2:
    print('A')
else:
    print('B')