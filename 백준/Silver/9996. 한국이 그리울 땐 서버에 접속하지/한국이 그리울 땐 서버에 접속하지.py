import sys
input=sys.stdin.readline

n=int(input())
p=input().strip().split('*')
n1, n2 = len(p[0]), len(p[1])
for _ in range(n):
    s=input().strip()
    if len(s)<(n1+n2):
        print('NE')
        continue
    pre=s[:n1]
    sub=s[-n2:]
    if pre==p[0] and sub==p[1]:
        print('DA')
    else:
        print('NE')