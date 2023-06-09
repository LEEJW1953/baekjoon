import sys
input=sys.stdin.readline

def compare(x, y, com):
    if com=='<':
        if x>y:
            return False
    elif com=='>':
        if x<y:
            return False
    return True

def f(x):
    global tmp, minn, maxx
    if x==k+1:
        if not minn:
            minn=tmp
        maxx=tmp
        return
    for i in range(10):
        if vis[i]:
            continue
        if x==0 or compare(int(tmp[x-1]), i, arr[x-1]):
            tmp+=str(i)
            vis[i]=1
            f(x+1)
            tmp=tmp[:-1]
            vis[i]=0

k=int(input())
arr=list(input().split())
tmp=''
vis=[0]*10
minn=0
maxx=0
f(0)
print(maxx)
print(minn)