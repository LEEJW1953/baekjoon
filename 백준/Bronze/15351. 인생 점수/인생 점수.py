import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    s=list(input().strip())
    total=0
    for i in s:
        if 65<=ord(i)<98:
            total+=ord(i)-64
    print(total if total!=100 else 'PERFECT LIFE')