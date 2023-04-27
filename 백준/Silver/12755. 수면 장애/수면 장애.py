import sys
input=sys.stdin.readline

t=int(input())-1
for i in range(10):
    c=(i+1)*9*10**i
    if c<t:
        t-=c
    else:
        s1=t//(i+1)
        s2=t%(i+1)
        print(str(10**i+s1)[s2])
        break