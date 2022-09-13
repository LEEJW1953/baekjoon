import sys
input=sys.stdin.readline

ww={}
def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        ww[a, b, c]=1
        return ww[a, b, c]
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    elif a<b and b<c:
        if (a, b, c) in ww:
            return ww[a, b, c]
        else:
            ww[a, b, c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return ww[a, b, c]
    else:
        if (a, b, c) in ww:
            return ww[a, b, c]
        else:
            ww[a, b, c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return ww[a, b, c]

while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print('w(%s, %s, %s) ='%(a, b, c), w(a, b, c) )