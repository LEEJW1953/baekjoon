import sys
input=sys.stdin.readline

def check(bcount, wcount):
    if b<bcount:
        return 0
    if wcount<w:
        return 1
    else:
        return 2

def add(x, y):
    global bcount, wcount
    if g[x:y]=='B':
        bcount+=1
    elif g[x:y]=='W':
        wcount+=1

def sub(x, y):
    global bcount, wcount
    if g[x:y]=='B':
        bcount-=1
    elif g[x:y]=='W':
        wcount-=1

n, b, w = map(int, input().split())
g=input().strip()
ans=0
left, right = 0, 1
bcount, wcount = 0, 0
add(left, right)
while left<n:
    tmp=check(bcount, wcount)
    if tmp==2:
        ans=max(ans, bcount+wcount)
        right+=1
        add(right-1, right)
    elif tmp==1:
        right+=1
        add(right-1, right)
    else:
        left+=1
        sub(left-1, left)
    if right>n:
        right=n
        left+=1
        sub(left-1, left)
print(ans)