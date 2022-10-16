import sys
input=sys.stdin.readline

def mul(x, y):
    if y==1:
        return x%c
    else:
        tmp=mul(x, y//2)
        if y%2==0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c
    return

a, b, c = map(int,input().split())
print(mul(a, b))