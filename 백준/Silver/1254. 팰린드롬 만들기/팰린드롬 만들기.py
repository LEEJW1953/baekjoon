import sys
input=sys.stdin.readline

def check(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            return False
    return True

s=input().strip()
n=len(s)
for i in range(n):
    if check(s[i:]):
        print(n+i)
        break