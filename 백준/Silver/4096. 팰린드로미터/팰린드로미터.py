import sys
input=sys.stdin.readline

def check(x):
    for i in range(len(x)//2):
        if x[i]!=x[len(x)-1-i]:
            return False
    return True

while True:
    n=input().strip()
    if n=='0':
        break
    l=len(n)
    ans=0
    while True:
        if check(n):
            print(ans)
            break
        n=str(int(n)+1).zfill(l)
        ans+=1