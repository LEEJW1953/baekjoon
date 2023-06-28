import sys
input=sys.stdin.readline

n=int(input())
i=n//5
while i>=0:
    tmp=n-i*5
    if not tmp:
        print(i)
        exit(0)
    else:
        tmp1=tmp%3
        if tmp1:
            i-=1
        else:
            print(i+tmp//3)
            exit(0)
print(-1)