import sys
input=sys.stdin.readline

def isGood(s):
    for i in range(1, 1+n//2):
        t1=s[-i:]
        t2=s[-2*i:-i]
        if t1==t2:
            return False
    return True

def track(s):
    if s and not isGood(s):
        return
    else:
        if len(s)==n:
            print(s)
            exit(0)
    for i in range(1, 4):
        if len(s)!=0 and str(i)==s[-1]:
            continue
        s+=str(i)
        track(s)
        s=s[:-1]

n=int(input())
track('')